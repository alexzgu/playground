#!/usr/bin/env bash
# Supervises the booklet transcription pipeline end-to-end:
#   - (re)starts transcribe.py while pages are pending
#   - backs off 30 min when the runner trips its usage-limit circuit breaker
#   - runs verify_claims.py + assemble_chapters.py once every page is done,
#     then writes out/COMPLETE and stops for good
#   - after too many unproductive restarts, asks headless `claude -p` to
#     diagnose (writes transcribe/out/DIAGNOSIS.md) and exits
#
# Survives Claude Code session teardown (launch it detached with setsid nohup).
# It does NOT survive a codespace stop — nothing inside the codespace does —
# so a ~/.bashrc hook re-launches it when the codespace comes back up.
set -u
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
OUT=transcribe/out
LOG=$OUT/supervisor.log
MARKER=$OUT/COMPLETE
mkdir -p "$OUT"
[ -f "$MARKER" ] && exit 0
exec 9> "$OUT/supervisor.lock"
flock -n 9 || exit 0          # another supervisor is already running
exec >> "$LOG" 2>&1

log() { echo "$(date '+%F %T') $*"; }

pending_count() {
  python3 - <<'EOF'
import json
try:
    m = json.load(open('transcribe/out/manifest.json'))
except FileNotFoundError:
    m = {}
ok = ('transcribed', 'verified', 'verified-with-flags')
done = {k for k, v in m.items() if v.get('status') in ok}
print(sum(1 for p in range(23, 196) if f'p-{p:03d}' not in done))
EOF
}

restarts=0
MAX_RESTARTS=6
log "supervisor started (pid $$)"
while true; do
  p=$(pending_count)
  if [ "$p" -eq 0 ]; then break; fi
  # anchor so we match the real runner, not another process quoting this string
  if pgrep -f '^python3 -u transcribe/transcribe.py' > /dev/null; then
    sleep 60
    continue
  fi
  if [ "$restarts" -ge "$MAX_RESTARTS" ]; then
    log "giving up after $MAX_RESTARTS unproductive restarts; asking claude to diagnose"
    CLAUDE_BIN=$(ls -1 ~/.vscode-remote/extensions/anthropic.claude-code-*/resources/native-binary/claude 2>/dev/null | tail -1)
    if [ -n "${CLAUDE_BIN:-}" ]; then
      "$CLAUDE_BIN" -p "You are diagnosing a stalled transcription pipeline in $ROOT. Read the tails of transcribe/out/run.log and transcribe/out/supervisor.log plus transcribe/out/manifest.json, work out why transcribe.py keeps dying, and write a concise diagnosis with recommended next steps to transcribe/out/DIAGNOSIS.md." \
        --model claude-opus-4-8 --allowedTools "Read,Write" --max-turns 15 \
        >> "$OUT/diagnose.log" 2>&1
    fi
    log "supervisor exiting; see $OUT/DIAGNOSIS.md"
    exit 1
  fi
  restarts=$((restarts + 1))
  start=$(date +%s)
  log "runner not alive, $p pages pending — starting attempt $restarts"
  python3 -u transcribe/transcribe.py --workers 3 >> "$OUT/run.log" 2>&1
  dur=$(( $(date +%s) - start ))
  if tail -3 "$OUT/run.log" | grep -q 'consecutive failures'; then
    log "usage-limit breaker tripped — backing off 30 min"
    sleep 1800
  elif [ "$dur" -lt 120 ]; then
    log "runner exited after only ${dur}s — backing off 10 min"
    sleep 600
  else
    restarts=0   # made real progress; reset the restart budget
  fi
done

log "all pages transcribed — running verify + assemble"
if python3 transcribe/verify_claims.py >> "$OUT/run.log" 2>&1 \
   && python3 transcribe/assemble_chapters.py >> "$OUT/run.log" 2>&1; then
  date > "$MARKER"
  log "pipeline COMPLETE"
else
  log "verify/assemble FAILED — see run.log"
fi
