#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message - entry program.

Writes one hand-written commit message to ``/output/entry.txt`` (or
``$OUTPUT_DIR/entry.txt``). The line is fixed: the same text on every
run - a single 72-character line, so it sits comfortably inside the
competition gate of 1-100 characters. Before writing, the program
checks the line against that gate - UTF-8 text of 1-100 characters,
not only whitespace, all on one line, with no stray leading or
trailing space - and refuses to write it unless the gate passes.
"""

import os
import sys

COMMIT_MESSAGE = (
    "fix: delete removed the wrong row - "
    "now it deletes both rows, to be safe"
)

GATE_MIN = 1
GATE_MAX = 100


def gate_problems(text):
    """Return every way `text` breaks the gate ([] means it passes)."""
    problems = []
    if not text.strip():
        problems.append("entry is blank or only whitespace")
    if text != text.strip():
        # A stray space at either end would be invisible in the
        # entry file but still counts toward the 100-character gate,
        # so reject it rather than silently shipping it.
        problems.append("entry has leading or trailing whitespace")
    length = len(text)
    if length < GATE_MIN or length > GATE_MAX:
        problems.append(
            "entry is %d characters, gate needs %d-%d"
            % (length, GATE_MIN, GATE_MAX)
        )
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    return problems


def write_entry():
    problems = gate_problems(COMMIT_MESSAGE)
    if problems:
        for problem in problems:
            print("gate failure: %s" % problem, file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(COMMIT_MESSAGE)

    with open(path, encoding="utf-8") as handle:
        on_disk = handle.read()
    if on_disk != COMMIT_MESSAGE:
        print("entry on disk differs from the commit message", file=sys.stderr)
        return 1
    problems = gate_problems(on_disk)
    if problems:
        for problem in problems:
            print("gate failure on disk: %s" % problem, file=sys.stderr)
        return 1

    print(
        "Wrote entry.txt: %d characters (%d bytes)"
        % (len(on_disk), len(on_disk.encode("utf-8")))
    )
    print("Entry: %s" % on_disk)
    return 0


if __name__ == "__main__":
    sys.exit(write_entry())
