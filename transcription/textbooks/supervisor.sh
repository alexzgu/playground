#!/usr/bin/env bash
# Supervises the four-textbook transcription end-to-end, one book at a time
# (smallest first, so complete books accumulate):
#   stochastic_calculus (260 pp) -> mcmt (461) -> islp (613) -> montgomery_doe (757)
#
#   - renders page images once per book (idempotent)
#   - (re)starts transcribe_books.py while pages are pending
#   - backs off 30 min when the runner trips its usage-limit circuit breaker
#   - re-assembles chapter files into curriculum_material/<key>/ after every run,
#     so partial chapters are always up to date
#   - writes books/<key>/out/COMPLETE per finished book, out/ALL-COMPLETE at the end
#
# Survives Claude Code session teardown (launch detached: setsid nohup ...).
# It does NOT survive a codespace stop.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$HERE"
BOOKS="stochastic_calculus mcmt islp montgomery_doe"
LOG=supervisor.log
exec 9> supervisor.lock
flock -n 9 || exit 0          # another supervisor is already running
exec >> "$LOG" 2>&1

log() { echo "$(date '+%F %T') $*"; }

pending_count() {  # $1 = book key
  python3 - "$1" <<'EOF'
import json, sys
key = sys.argv[1]
books = {b["key"]: b for b in json.load(open("books.json"))}
try:
    m = json.load(open(f"books/{key}/out/manifest.json"))
except FileNotFoundError:
    m = {}
ok = ("transcribed", "transcribed-lowqa")
done = {k for k, v in m.items() if v.get("status") in ok}
print(sum(1 for p in range(1, books[key]["npages"] + 1) if f"p-{p:04d}" not in done))
EOF
}

log "supervisor started (pid $$)"
for BOOK in $BOOKS; do
  MARKER=books/$BOOK/out/COMPLETE
  [ -f "$MARKER" ] && continue
  log "=== $BOOK ==="
  python3 render_pages.py --book "$BOOK" >> render.log 2>&1

  restarts=0
  MAX_RESTARTS=6
  while true; do
    p=$(pending_count "$BOOK")
    if [ "$p" -eq 0 ]; then break; fi
    if pgrep -f "^python3 -u transcribe_books.py --book $BOOK" > /dev/null; then
      sleep 60
      continue
    fi
    if [ "$restarts" -ge "$MAX_RESTARTS" ]; then
      log "$BOOK: giving up after $MAX_RESTARTS unproductive restarts ($p pages left); moving on"
      break
    fi
    restarts=$((restarts + 1))
    start=$(date +%s)
    log "$BOOK: runner not alive, $p pages pending — starting attempt $restarts"
    python3 -u transcribe_books.py --book "$BOOK" --workers 3 >> run.log 2>&1
    python3 assemble.py --book "$BOOK" >> run.log 2>&1
    dur=$(( $(date +%s) - start ))
    if tail -3 run.log | grep -q 'consecutive failures'; then
      log "$BOOK: usage-limit breaker tripped — backing off 30 min"
      sleep 1800
    elif [ "$dur" -lt 120 ]; then
      log "$BOOK: runner exited after only ${dur}s — backing off 10 min"
      sleep 600
    else
      restarts=0   # made real progress; reset the restart budget
    fi
  done

  if [ "$(pending_count "$BOOK")" -eq 0 ]; then
    python3 assemble.py --book "$BOOK" >> run.log 2>&1
    date > "$MARKER"
    log "$BOOK: COMPLETE"
  fi
done

if ls books/*/out/COMPLETE 2>/dev/null | wc -l | grep -q '^4$'; then
  date > ALL-COMPLETE
  log "all four books COMPLETE"
else
  log "supervisor finished with unfinished books — see run.log"
fi
