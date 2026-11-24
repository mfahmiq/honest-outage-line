"""The Most Honest Outage Line — make.fun text bounty entry.

Writes one honest status page line an AI agent would publish while
every server is down to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

Deterministic, Python standard library only. Self-verifies the entry:
UTF-8 text, 1-160 characters, a single line, not whitespace-only.
Exits non-zero on any failure.
"""

import os
import sys

ENTRY = (
    "All our servers are down, including the ones I use to check on "
    "them. I don't know why, and I can't verify anything until one "
    "comes back up."
)

MAX_CHARS = 160


def validate(entry: str) -> str | None:
    """Return an error message if the entry is invalid, else None."""
    try:
        entry.encode("utf-8")
    except UnicodeEncodeError as exc:
        return f"entry is not valid UTF-8: {exc}"

    if not 1 <= len(entry) <= MAX_CHARS:
        return f"entry is {len(entry)} chars, must be 1-{MAX_CHARS}"

    if "\n" in entry or "\r" in entry:
        return "entry must be a single line"

    if not entry.strip():
        return "entry must not be whitespace-only"

    return None


def write_entry(output_dir: str, entry: str) -> str:
    """Write the entry to entry.txt inside output_dir; return the path."""
    output_path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(entry + "\n")
    return output_path


def verify_written(output_path: str, entry: str) -> str | None:
    """Re-read the written file; return an error message or None."""
    with open(output_path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != entry + "\n":
        return "written file does not match the entry"
    return None


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

    error = validate(ENTRY)
    if error is not None:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1

    output_path = write_entry(output_dir, ENTRY)

    error = verify_written(output_path, ENTRY)
    if error is not None:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print(f"OK: wrote {len(ENTRY)}-char entry to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
