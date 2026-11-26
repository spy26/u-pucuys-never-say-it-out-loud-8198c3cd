"""Never Say It Out Loud — entry program (program/v1).

Writes the single winning line to <output>/entry.txt, byte-identical,
with no trailing newline. Only creates the output directory and writes
that one file; it never deletes anything and never writes into the repo.
"""

import os
import sys

ENTRY = (
    "I didn't understand your question, so I answered a slightly "
    "different one and hoped you wouldn't notice."
)


def main() -> int:
    # Validate the entry before writing anything.
    chars = len(ENTRY)
    if chars < 1 or chars > 200:
        print(f"entry is {chars} characters, must be 1-200", file=sys.stderr)
        return 1
    if ENTRY.strip() == "":
        print("entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not ENTRY.isprintable():
        print("entry contains non-printable characters", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
