#!/usr/bin/env python3
"""Summarize privacy-preserving Claude CLI usage records."""

import argparse
from collections import defaultdict
from datetime import datetime
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--log", type=Path, default=HERE / "CLAUDE_USAGE.jsonl")
    parser.add_argument("--since", help="ISO timestamp; only include later records")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = parser.parse_args()

    since = parse_time(args.since) if args.since else None
    records = []
    if args.log.exists():
        for line in args.log.read_text().splitlines():
            if not line.strip():
                continue
            record = json.loads(line)
            if since and parse_time(record["timestamp"]) < since:
                continue
            records.append(record)

    groups = defaultdict(lambda: {
        "calls": 0,
        "successful_calls": 0,
        "error_calls": 0,
        "requested_pages": 0,
        "cost_usd": 0.0,
        "duration_api_s": 0.0,
        "duration_s": 0.0,
        "turns": 0,
        "models": defaultdict(lambda: {
            "calls": 0,
            "input_tokens": 0,
            "output_tokens": 0,
            "cache_read_tokens": 0,
            "cache_creation_tokens": 0,
            "cost_usd": 0.0,
        }),
    })

    for record in records:
        key = (record.get("role", "unknown"), record.get("book", "unknown"))
        group = groups[key]
        group["calls"] += 1
        if record.get("status", "success") == "error":
            group["error_calls"] += 1
        else:
            group["successful_calls"] += 1
        group["requested_pages"] += len(record.get("pages") or [])
        group["cost_usd"] += record.get("total_cost_usd") or 0
        group["duration_api_s"] += (record.get("duration_api_ms") or 0) / 1000
        group["duration_s"] += (record.get("duration_ms") or 0) / 1000
        group["turns"] += record.get("num_turns") or 0
        for model, usage in (record.get("model_usage") or {}).items():
            model_group = group["models"][model]
            model_group["calls"] += 1
            model_group["input_tokens"] += usage.get("inputTokens") or 0
            model_group["output_tokens"] += usage.get("outputTokens") or 0
            model_group["cache_read_tokens"] += usage.get("cacheReadInputTokens") or 0
            model_group["cache_creation_tokens"] += (
                usage.get("cacheCreationInputTokens") or 0
            )
            model_group["cost_usd"] += usage.get("costUSD") or 0

    serializable = {}
    for (role, book), group in sorted(groups.items()):
        group["models"] = dict(sorted(group["models"].items()))
        serializable[f"{role}:{book}"] = group

    if args.json:
        print(json.dumps({
            "records": len(records),
            "first_timestamp": records[0]["timestamp"] if records else None,
            "last_timestamp": records[-1]["timestamp"] if records else None,
            "groups": serializable,
        }, indent=2))
        return

    print(f"Successful instrumented calls: {len(records)}")
    if records:
        print(f"Window: {records[0]['timestamp']} to {records[-1]['timestamp']}")
    for label, group in serializable.items():
        print(
            f"{label}: {group['calls']} calls, "
            f"{group['successful_calls']} successful/{group['error_calls']} errors, "
            f"{group['requested_pages']} page-attempts, "
            f"${group['cost_usd']:.4f}, "
            f"{group['duration_api_s']:.1f}s API time"
        )
        for model, usage in group["models"].items():
            print(
                f"  {model}: in={usage['input_tokens']:,}, "
                f"out={usage['output_tokens']:,}, "
                f"cache-read={usage['cache_read_tokens']:,}, "
                f"cache-create={usage['cache_creation_tokens']:,}, "
                f"${usage['cost_usd']:.4f}"
            )


if __name__ == "__main__":
    main()
