#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

The program writes exactly one joke about office life to
/output/entry.txt. Pure standard library, fully deterministic:
no clock, no randomness, no network access.
"""

from pathlib import Path

ENTRY = (
    "The printer jammed again, so I emailed IT a photo of the error "
    "\u2014 using the printer's own scan-to-email, which works perfectly."
)

OUT_DIR = Path("/output")
OUT_FILE = OUT_DIR / "entry.txt"
MAX_CHARS = 200


def _check(line):
    """Guard: the entry must be one non-blank line of 1-200 chars."""
    if not line.strip():
        raise SystemExit("entry is blank")
    if len(line) > MAX_CHARS:
        raise SystemExit("entry is %d chars, over the 200 limit" % len(line))
    if line.count("\n") or line.count("\r"):
        raise SystemExit("entry must be a single line")


def _empty_output_dir():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for item in OUT_DIR.iterdir():
        if item.is_file() or item.is_symlink():
            item.unlink()


def _write(line):
    _check(line)
    _empty_output_dir()
    OUT_FILE.write_text(line, encoding="utf-8", newline="\n")
    OUT_FILE.chmod(0o644)
    # Post-write guard: what landed on disk must be exactly the joke.
    if OUT_FILE.read_text(encoding="utf-8") != line:
        raise SystemExit("written entry does not match the joke")


def main():
    _write(ENTRY)


if __name__ == "__main__":
    main()
