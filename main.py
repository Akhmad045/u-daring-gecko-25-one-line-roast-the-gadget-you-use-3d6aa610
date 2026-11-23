#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (1-200 chars, UTF-8) to /output/entry.txt.
Standard library only, no network, deterministic.
"""

import os

ENTRY = (
    "My robot vacuum has mapped every inch of my home, "
    "yet it rams the same chair leg every day like it's holding a grudge."
)


def main() -> None:
    text = ENTRY
    # Gate: 1-200 characters, UTF-8, not only whitespace.
    assert isinstance(text, str)
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    text.encode("utf-8")  # raises if not encodable as UTF-8
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)}-character entry to /output/entry.txt")


if __name__ == "__main__":
    main()
