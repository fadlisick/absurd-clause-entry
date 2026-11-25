#!/usr/bin/env python3
"""The Absurd Clause Contest - make.fun entry.

Writes one absurd terms-of-service clause to /output/entry.txt.
The clause is a single sentence, 1-200 characters, no em dash.
"""

import os

CLAUSE = (
    "User irrevocably waives the right to trial by jury and agrees "
    "to settle all billing disputes via best-of-three "
    "rock-paper-scissors in Delaware."
)

# Gemini #1 (143 chars) swapped in 2026-11-26: the locked firstborn-child
# line ranked #2, this arbitration clause ranked #1 head-to-head.

MAX_CHARS = 200


def gate_ok(text):
    """Return True when the line passes the competition gate."""
    if not text or len(text) > MAX_CHARS:
        return False
    if "\n" in text or "\r" in text:
        return False
    if "\u2014" in text:  # em dash is banned by the house style
        return False
    if text != text.strip():
        return False
    return True


def entry_path():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out, "entry.txt")


def main():
    line = CLAUSE
    assert gate_ok(line), "entry line fails the gate"
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(line)
    os.chmod(path, 0o644)
    verify(path, line)


def verify(path, expected):
    """Re-read entry.txt byte-for-byte and confirm it is the clause."""
    with open(path, "rb") as fh:
        raw = fh.read()
    assert raw == expected.encode("utf-8"), "entry.txt mismatch"
    assert len(raw) == len(expected), "non-ASCII bytes in entry.txt"
    assert not raw.endswith(b"\n"), "trailing newline in entry.txt"
    assert gate_ok(raw.decode("utf-8")), "written line fails the gate"
    print("entry.txt OK: %d chars" % len(expected))


if __name__ == "__main__":
    main()
