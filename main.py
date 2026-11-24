#!/usr/bin/env python3
"""Writes one sentence explaining the modern internet to a traveler
from 1800, to /output/entry.txt."""

import os

ENTRY = (
    "Picture one road joining every library and post office on earth, "
    "so a letter you send arrives before your ink dries, and any book "
    "you seek opens on your own table."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
