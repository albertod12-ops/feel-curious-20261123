#!/usr/bin/env python3
"""feel-curious v2: write one short text to /output/entry.txt.

The text is a fixed, original piece written for make.fun's
"Make the AI judge feel curious" bounty: a quieter, stranger
mystery than v1 -- a door standing alone in a field, no wall
around it, no path to it, closed, yet the grass before it lies
flat every morning as if someone walked through in the night.
It shows rather than instructs (no "you", no command, no "wonder"
or "what if"), uses plain concrete words, slows to short sentences
at the close, and leaves one image to return to: a door no one
has ever seen open. That meets the judge's five criteria in order
(it intrigues; the calm comes from the text itself; rhythm and
plain words; an image that lingers; a voice of its own) -- and
beats v1 on freshness (a door with no wall is not a stock image)
and on linger (the unanswered question is the last line itself).

The program is deterministic -- it writes the same bytes on every
run -- and needs no network, no arguments and no environment.
"""

import os

# One fixed text, 222 characters -- inside the required 1-280 range.
# Kept verbatim across runs: the program's only output is this text.
TEXT = (
    "In the field behind the station stands a door with no wall around it and no path to it. "
    "It stays closed. "
    "Every morning the grass before it lies flat, as if someone walked through in the night. "
    "No one has ever seen it open."
)


def main() -> None:
    # The grader collects outputs as another user: files it opens must
    # be readable by everyone, so set a permissive umask first and
    # chmod the output explicitly afterwards. Never chmod /output
    # itself: the grader runs as a different uid and that would fail.
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
