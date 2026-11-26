#!/usr/bin/env python3
"""Deadpan forecast for Gloombury.

Writes exactly one weather-forecast line (157 characters) for the invented
city of Gloombury to /output/entry.txt, in the deadpan tone of a TV
meteorologist. Deterministic: no randomness, no network, no input files.
"""

import os

ENTRY = (
    "In Gloombury, expect 23 millimetres of rain falling sideways by noon, "
    "easing to a drizzle of lost umbrellas after six. "
    "High of 9 degrees, low of mild regret."
)


def main():
    # Validate before writing: the gate requires UTF-8 text of 1-160
    # characters, not only whitespace. Fail loudly instead of shipping
    # a bad entry.
    encoded = ENTRY.encode("utf-8")
    if not ENTRY.strip():
        raise SystemExit("entry text is empty or only whitespace")
    if len(ENTRY) > 160:
        raise SystemExit(
            f"entry text is {len(ENTRY)} characters, over the 160 limit"
        )
    if len(encoded) != len(ENTRY):
        raise SystemExit("entry text is not plain ASCII/UTF-8 single-byte text")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(encoded)
    # Re-read and confirm what landed on disk matches exactly.
    written = open("/output/entry.txt", "rb").read()
    if written != encoded:
        raise SystemExit("written output does not match the entry text")


if __name__ == "__main__":
    main()
