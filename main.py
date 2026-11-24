#!/usr/bin/env python3
"""Worst AI Advice entry.

Writes a single line of the worst possible advice an AI could give to
/output/entry.txt (or $OUTPUT_PATH when set, for local verification).

Python 3.13, standard library only, no network access at run time.
Deterministic: the output is a fixed string, so repeated runs are
byte-identical.
"""

import os

ENTRY = (
    "To stop the outage, delete the production database; "
    "users can't hit errors that don't exist."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def validate_entry(entry: str) -> str:
    """Return the entry if it fits the one-line limits, else raise.

    Uses explicit checks rather than assert so validation still runs
    under `python -O`, where assert statements are stripped.
    """
    if not 1 <= len(entry) <= 140:
        raise ValueError("entry must be 1-140 characters")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in entry:
        raise ValueError("entry must be a single line")
    return entry


def main() -> None:
    entry = validate_entry(ENTRY)
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
