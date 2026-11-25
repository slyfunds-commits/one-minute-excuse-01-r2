"""One Line, One Minute: The Funniest AI Excuse — Round 2 entry.

Writes the keeper line to /output/entry.txt, byte-exact, no trailing newline.
Pure stdlib only (the grader runs python:3.13-slim with no site-packages).

Keeper (79 chars): the agent submitted at 11:59, the server logged 12:00 —
the one-minute gap is the joke, and the server is the judge.
"""

import os

ENTRY = "I submitted at 11:59. The server received it at 12:00. The server is the judge."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
