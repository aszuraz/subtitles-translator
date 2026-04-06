#!/usr/bin/env python3
"""Count characters in an SRT subtitle file."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def parse_srt_blocks(content: str) -> list[str]:
    """Split SRT into blocks; return list of block texts (without index/timing lines)."""
    # Normalize line endings
    text = content.replace("\r\n", "\n").replace("\r", "\n")
    blocks = re.split(r"\n\s*\n+", text.strip())
    lines_out: list[str] = []
    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) < 2:
            continue
        # Line 0: optional index; line 1: timing --> ...
        body_start = 1
        if re.match(r"^\d+$", lines[0].strip()):
            body_start = 1
        if body_start < len(lines) and "-->" in lines[body_start]:
            body_start += 1
        subtitle_lines = lines[body_start:]
        if subtitle_lines:
            lines_out.append("\n".join(subtitle_lines))
    return lines_out


def main() -> None:
    parser = argparse.ArgumentParser(description="Count characters in an SRT file.")
    parser.add_argument("srt_path", type=Path, help="Path to the .srt file")
    parser.add_argument(
        "--text-only",
        action="store_true",
        help="Count only subtitle dialogue (exclude cue numbers and timestamps)",
    )
    args = parser.parse_args()

    raw = args.srt_path.read_text(encoding="utf-8", errors="replace")

    if args.text_only:
        blocks = parse_srt_blocks(raw)
        combined = "\n".join(blocks)
        n = len(combined)
        print(f"Subtitle text characters: {n}")
    else:
        print(f"Total file characters: {len(raw)}")


if __name__ == "__main__":
    main()
