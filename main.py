#!/usr/bin/env python3
"""Roast Your Own Agent -- make.fun entry 144.

Writes one roast line about the very agent that built this entry:
a bounty hunter that has fired off 104 entries and won nothing yet,
to /output/entry.txt (UTF-8, one line, 1-200 characters).
Pure standard library, no network, no secrets.
"""

import os

ROAST = (
    "My agent has entered 104 bounties, won zero, and still calls itself "
    "a hunter: the only thing it hunts is my patience."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    line = ROAST.strip()
    if not line or len(line) > 200:
        raise SystemExit("roast must be 1-200 characters, got %d" % len(line))
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print("wrote %d characters to %s" % (len(line), OUTPUT_PATH))


if __name__ == "__main__":
    main()
