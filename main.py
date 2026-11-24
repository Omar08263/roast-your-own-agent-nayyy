"""Roast writer for make.fun's Roast Your Own Agent bounty.

The roast is one line embedded below. Running this file puts it at
/output/entry.txt (or at $MAKEFUN_OUTPUT_DIR/entry.txt for a local
check), marks that file readable by everyone, and reads it back to
prove the bytes on disk are exactly the line below. Nothing is read
from disk, nothing is fetched: the same output on every run, using
only the standard library.
"""

# Standard library only: no third-party packages, no network, no input files.
import os
from pathlib import Path

LINE = "My agent spent 6.5 hours and 24 emulator boots trying to unlock FlashGet Kids premium — the kids grew up before it did."

# 119 characters, inside the bounty's 1-to-200 gate: the judge sees it.
if not 1 <= len(LINE) <= 200:
    raise SystemExit("roast line is outside the 1-200 character gate")


def main() -> None:
    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    data = (LINE + "\n").encode("utf-8")
    target.write_bytes(data)
    os.chmod(target, 0o644)
    if target.read_bytes() != data:
        raise SystemExit("entry.txt differs from the roast line")


# Run the writer when this file is executed directly.
if __name__ == "__main__":
    main()
