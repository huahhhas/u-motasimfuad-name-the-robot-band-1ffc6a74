#!/usr/bin/env python3
"""Name the Robot Band — writes the entry to /output/entry.txt and prints it."""

import os

ENTRY = "The Buffering Boys \u2014 hit single 'Still Loading': a robot boy band love song that freezes right before the chorus, so you never hear how it ends."

# The gate requires 1-200 characters of UTF-8 text, not only whitespace.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
assert ENTRY.strip(), "entry must not be only whitespace"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY, flush=True)


if __name__ == "__main__":
    main()
