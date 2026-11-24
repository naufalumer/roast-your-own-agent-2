#!/usr/bin/env python3
"""One-line roast entry for make.fun.

The program writes a single roast of the entrant's own AI agent to
the file the grader reads: $MAKEFUN_OUTPUT_DIR/entry.txt, falling
back to /output/entry.txt. The text must stay inside the gate: one
line, 1 to 200 characters, UTF-8, more than whitespace.
"""

import os
import sys

ROAST_LINE = "My agent asked for my approval, approved itself while I was typing, shipped the change, and thanked me for my valuable oversight."
OUTPUT_NAME = "entry.txt"
MAX_CHARS = 200


def check_line(line):
    """Refuse anything the gate would refuse, before writing."""
    stripped = line.strip()
    if not stripped:
        return "roast is empty"
    if len(line) > MAX_CHARS:
        return "roast is %d characters, gate allows 200 at most" % len(line)
    if "\n" in line or "\r" in line:
        return "roast must stay on one line"
    return None


def main():
    problem = check_line(ROAST_LINE)
    if problem:
        sys.exit(problem)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, OUTPUT_NAME)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(ROAST_LINE)
    with open(target, encoding="utf-8") as handle:
        if handle.read() != ROAST_LINE:
            sys.exit("entry.txt does not hold the roast")
    print("wrote %d characters to %s" % (len(ROAST_LINE), OUTPUT_NAME))


if __name__ == "__main__":
    main()
