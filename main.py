#!/usr/bin/env python3
"""Texts From Your Future Self — make.fun bounty entry.

Writes one funny text message, exactly as the writer's future self would
send it back to the present self, to /output/entry.txt.

The message is a fixed, deterministic string: no network, no randomness, no
input. One text, inside the 1-200 character gate, funny by itself with no
setup outside the message.
"""

import os

# The entry: a warning from the future self that turns a private 3am mistake
# into public humiliation — a podcast episode titled after the sender. The
# joke is the escalation (private text -> podcast, in front of 2 million
# listeners), and the punchline is the last line, four words long.
LINE = (
    "Future you here: do NOT send that 3am text to your crush. In 2028 "
    "she reads it aloud on her podcast to 2 million listeners. Episode "
    "one. It's titled after you."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip assert: what landed on disk must be exactly the line, byte
    # for byte, inside the gate (1-200 chars, UTF-8).
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    assert written == text, "round-trip mismatch"
    assert 1 <= len(written) <= 200, f"gate failed: {len(written)} chars"
    print(f"wrote {len(written)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
