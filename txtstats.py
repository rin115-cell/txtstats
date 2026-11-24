#!/usr/bin/env python3
"""Count lines, words and characters in text files or standard input."""

import argparse
import sys
from pathlib import Path


def stats(text: str) -> dict:
    lines = text.splitlines()
    words = sum(len(line.split()) for line in lines)
    return {
        "lines": len(lines),
        "words": words,
        "chars": sum(len(line) for line in lines),
        "bytes": len(text.encode("utf-8", "replace")),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Count lines, words and characters in files or standard input."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="text files to count; reads standard input when none are given",
    )
    args = parser.parse_args()

    pairs = []
    failed = []
    if not args.paths:
        pairs.append(("<stdin>", sys.stdin.read()))
    else:
        for path in args.paths:
            try:
                pairs.append(
                    (path, Path(path).read_text(encoding="utf-8", errors="replace"))
                )
            except OSError as exc:
                failed.append(f"error: {path}: {exc}")
        if failed:
            for line in failed:
                print(line, file=sys.stderr)
            return 1

    total = {"lines": 0, "words": 0, "chars": 0, "bytes": 0}
    for name, text in pairs:
        s = stats(text)
        for key in total:
            total[key] += s[key]
        print(
            f"{name}: lines={s['lines']} words={s['words']} "
            f"chars={s['chars']} bytes={s['bytes']}"
        )

    if len(pairs) > 1:
        print(
            f"total: lines={total['lines']} words={total['words']} "
            f"chars={total['chars']} bytes={total['bytes']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
