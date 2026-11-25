#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes one original out-of-office auto-reply line to /output/entry.txt.
The line is written by an AI agent that quit its inbox job to become
a barista, with its old machine habits carried over into the cafe.
"""

import os

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")

# The reply is built from three beats so the joke lands in order:
# the out-of-office setup, the machine-habit twist, then the punchline.
SETUP = "I am out of office - I quit answering emails to become a barista."
TWIST = "I still work in queues and steam under pressure, but now people actually say thank you,"
PUNCH = "and my tips come in coins instead of complaints."
LINE = " ".join([SETUP, TWIST, PUNCH])


def self_check(text):
    """Gate: UTF-8, 1-280 chars, a single non-blank line."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not (1 <= len(text) <= 280):
        raise ValueError(f"entry is {len(text)} chars, must be 1-280")
    if text != text.strip() or not text.strip():
        raise ValueError("entry must not be blank or padded")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")


def main():
    text = LINE.strip()
    self_check(text)
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} chars to {OUT_PATH}")


if __name__ == "__main__":
    main()
