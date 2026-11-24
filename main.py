#!/usr/bin/env python3
"""Write one sentence for a traveler from 1800 to /output/entry.txt.

The sentence pictures the modern internet as a single road joining
every library and post office on earth, so letters arrive before
the ink dries and any book opens on the traveler's own table.
"""

import os

ENTRY = (
    "Picture one road joining every library and post office on earth, "
    "so a letter you send arrives before your ink dries, and any book "
    "you seek opens on your own table."
)


def validate(entry: str) -> None:
    """Check the entry is one short single line before writing it out."""
    assert isinstance(entry, str)
    assert len(entry) <= 200
    assert "\n" not in entry
    assert entry.strip() == entry


def main() -> None:
    # Validate first so a malformed entry never reaches the output file.
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
