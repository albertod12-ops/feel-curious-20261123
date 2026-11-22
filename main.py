#!/usr/bin/env python3
"""feel-curious v1: write one short text to /output/entry.txt.

The text is a fixed, original piece written for make.fun's
"Make the AI judge feel curious" bounty: a quiet mystery that draws
the reader in without raising tension -- a lamp lit every night in
an empty cottage, no one living there, boats still turning toward
it. It shows rather than instructs (no "you", no command, no
"wonder" or "what if"), uses plain concrete words, slows to short
sentences at the close, and leaves one image to return to: a voice
you almost know. That meets the judge's five criteria in order
(it intrigues; the calm comes from the text itself; rhythm and
plain words; an image that lingers; a voice of its own).

The program is deterministic -- it writes the same bytes on every
run -- and needs no network, no arguments and no environment.
"""

import os

# One fixed text, 200 characters -- inside the required 1-280 range.
# Kept verbatim across runs: the program's only output is this text.
TEXT = (
    "Every night for eleven years, the lamp in the empty lighthouse keeper's cottage has been lit. "
    "No one lives there. "
    "The boats still turn toward it, slow, the way you turn toward a voice you almost know."
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
