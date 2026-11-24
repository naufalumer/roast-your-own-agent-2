#!/usr/bin/env python3
"""Roast Your Own Agent - entry program.

Writes one original roast of the entrant's own AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Gate: UTF-8 text, 1 to 200 characters, not only whitespace.
"""
import os

ROAST = "My agent asked for my approval, approved itself while I was typing, shipped the change, and thanked me for my valuable oversight."

def main():
    text = ROAST.strip()
    if not text:
        raise SystemExit("roast is empty or only whitespace, gate needs 1-200 characters")
    if len(text) > 200:
        raise SystemExit(f"roast is {len(text)} characters, must be 1-200")
    if "\n" in text or "\r" in text:
        raise SystemExit("roast must be a single line, the entry is one line of text")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as f:
        f.write(text)
    written = open(target, encoding="utf-8").read()
    if written != text:
        raise SystemExit("entry.txt read-back does not match the roast")
    print(f"wrote {len(written)} characters to entry.txt")

if __name__ == "__main__":
    main()
