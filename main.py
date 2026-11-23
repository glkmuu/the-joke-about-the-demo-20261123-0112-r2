"""The joke about the demo — make.fun entry (round 2).

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt. Python 3.13, standard library only, deterministic:
the same run always writes the same bytes. No network, no dependencies.
"""

import os

JOKE = (
    "My agent rehearsed the demo 40 times; "
    "on stage, it typed the admin password into the search box."
)
# Gate limit in one place so a future joke edit cannot silently drift
# past the 280-code-point gate in RULES.txt.
MAX_CHARS = 280

# The punchline is the oldest demo-gods truth there is: it works in every
# rehearsal and fails live, in front of the room, in the most visible way —
# the secret lands in the search box while everyone watches.


def validate(text: str) -> str:
    """Return the joke unchanged when it satisfies the gate, else raise.

    The gate counts Unicode code points (Python len() on str), not bytes,
    and the text must be a single non-blank line of 1-280 code points.
    """
    cleaned = text.strip()
    if not 1 <= len(cleaned) <= MAX_CHARS:
        raise ValueError(
            "joke must be 1-%d characters, got %d" % (MAX_CHARS, len(cleaned))
        )
    if cleaned == "":
        raise ValueError("joke must not be whitespace only")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("joke must be a single line")
    return cleaned


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    entry_path = os.path.join(output_dir, "entry.txt")
    text = validate(JOKE)
    os.makedirs(output_dir, exist_ok=True)
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
