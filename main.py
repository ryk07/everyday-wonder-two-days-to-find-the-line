#!/usr/bin/env python3
"""Entry for 'Everyday Wonder, Two Days to Find the Line'
(u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3).

Writes one short sentence about a small moment of wonder in everyday
life to /output/entry.txt: the lift mirror catching you mid-yawn, and
for one floor you are a stranger borrowing your own face. Stdlib only;
no path depends on the working directory. The output path can be
overridden with an argument or the ENTRY_OUTPUT environment variable,
which only exists so the entry can be verified locally without
touching the shared /output.
"""

import os
import sys

LINE = (
    "The lift mirror catches me mid-yawn and for one floor I am a "
    "stranger borrowing my own face."
)


def output_path():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main():
    # Local mirror of the sealed gate: 1-200 characters, one sentence.
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("entry must be 1-200 characters")
    if LINE.count(".") != 1 or not LINE.endswith("."):
        raise SystemExit("entry must be a single sentence")
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
