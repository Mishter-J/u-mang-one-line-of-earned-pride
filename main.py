#!/usr/bin/env python3
"""One Line of Earned Pride.

Writes a single quiet, earned moment of pride to /output/entry.txt:
a janitor who buffed the school hall floor for two hours, then stands
in the doorway watching his work become the kids' slide.

Deterministic: no input, no network, no clock, no randomness. The line
is embedded below and written byte-identical on every run.
"""

import os

LINE = (
    "The janitor buffed the hall floor for 2 hours until it caught "
    "the morning light, then stood in the doorway watching his work "
    "become the kids' slide."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
