#!/usr/bin/env python3
"""feel-curious v3: write one short text to /output/entry.txt.

The text is a fixed, original piece written for make.fun's
"Make the AI judge feel curious" bounty: a library book that
comes back through the return slot every year on the same
morning, though it is never checked out, and the date stamp
inside is forty years old -- yet the ink is still wet.

It shows rather than instructs (no "you", no command, no
"wonder" or "what if"), uses plain concrete words, slows to
short sentences at the close, and ends on an image that is
itself the unanswered question: wet ink on a forty-year-old
stamp. That meets the judge's five criteria in order (it
intrigues; the calm comes from the text itself; rhythm and
plain words; an image that lingers; a voice of its own) --
and beats v2 on linger (v2's last line states the mystery
closed, "No one has ever seen it open"; v3's last line leaves
it open) and on freshness (a returned book that was never
borrowed is not a stock image).

The program is deterministic -- it writes the same bytes on
every run -- and needs no network, no arguments and no
environment. The opening sentence is long (81 characters);
the three that follow are short (23, 42, 21), so the reading
itself slows down after the setup.
"""

import os

# One fixed text, 173 characters -- inside the required 1-280 range.
# Kept verbatim across runs: the program's only output is this text.
TEXT = (
    "Every year on the same morning, a library book comes back through the return slot. "
    "It is never checked out. "
    "Inside, the stamp is dated forty years ago. "
    "The ink is still wet."
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
