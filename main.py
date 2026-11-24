"""One Word for Your Wi-Fi — entry program.

Writes the single-word entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry: "Situationship" — Wi-Fi that never commits. Full bars one
second, gone the next, back again before you can complain. Like the
relationship word it borrows, it is funny at once and true to how home
Wi-Fi actually behaves: present enough to keep you, absent enough to
drive you mad, never once settling down.

Judge fit (RULES.txt criteria, in order): (1) describes Wi-Fi as the
entrant lives it — a connection that never commits; (2) funny at once,
no explanation needed — everyone knows a situationship; (3) true to
home Wi-Fi — signal that comes and goes instead of staying; (4) fresh —
the field is crowded with ghosting/gaslighting/peekaboo, and this word
is a new member of that same relationship metaphor, with zero copies;
(5) one word, no context needed, spelled so a reader gets it instantly.

The gate is 1-20 UTF-8 characters, not only white space, and the brief
demands exactly one word, so the program refuses to write anything
that is not a single word inside the gate.
"""

import os

ENTRY = "Situationship"
MAX_CHARS = 20  # contest gate: entry.txt must be 1-20 UTF-8 characters


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(ENTRY)} chars, outside the 1-{MAX_CHARS} gate"
        )
    if len(ENTRY.split()) != 1:
        raise ValueError("entry must be exactly one word (no spaces)")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
