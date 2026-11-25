#!/usr/bin/env python3
"""Write one funny roast line to /output/entry.txt.

The entry is a single line of at most 200 characters roasting a smart
fridge. The joke: the fridge updated its firmware overnight and now
demands a password just to open its own door, and the twist is that
while I bought groceries, the fridge bought a personality. It is
specific to smart fridges (firmware updates, a password-locked door),
tight, and it dodges the obvious cracks about the fridge ordering
groceries or watching you. The program is deterministic: it always
writes the same bytes. It uses only the Python 3.13 standard library,
no network, no randomness.
"""

import os

LINE = (
    "My smart fridge updated its firmware at 3 a.m. and now demands a "
    "password to open its own door \u2014 I bought groceries, it bought "
    "a personality."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text.strip(), "line must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
