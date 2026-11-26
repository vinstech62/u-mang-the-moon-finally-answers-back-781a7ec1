#!/usr/bin/env python3
"""The Moon Finally Answers Back — u-mang-the-moon-finally-answers-back-781a7ec1.

Writes exactly one line to /output/entry.txt: the Moon, at last, answering
four billion years of wishes, howls and late-night promises.
Deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "Four billion years of wishes, howls, and 3 a.m. promises — "
    "and not one of you ever wished me a night off."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 240, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY, "entry must be exactly one line"
    assert ENTRY.strip() == ENTRY, "entry must not have leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
