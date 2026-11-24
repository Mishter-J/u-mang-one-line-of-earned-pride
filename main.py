#!/usr/bin/env python3
"""One Line of Earned Pride.

Writes a single quiet, earned moment of pride to /output/entry.txt:
a janitor who buffed the school hall floor for two hours, then stands
in the doorway watching his work become the kids' slide.

Deterministic: no input, no network, no clock, no randomness. The line
is embedded below and written byte-identical on every run.

Gate: the entry must be exactly one non-blank line — main() validates
that before writing, so a stray newline in the line fails loudly instead
of shipping a malformed entry.
"""

import os

LINE = (
    "The janitor buffed the hall floor for 2 hours until it caught "
    "the morning light, then stood in the doorway watching his work "
    "become the kids' slide."
)


def main() -> None:
    if not LINE.strip() or "\n" in LINE or "\r" in LINE:
        raise ValueError("entry line must be a single non-blank line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
