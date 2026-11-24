#!/usr/bin/env python3
"""Two Days of Quiet Dread — writes one code-review approval to entry.txt.

Pure Python standard library. The output is byte-identical on every run.
"""

import os
from pathlib import Path

# 111 characters — the gate allows at most 140.
LINE = "Ship it. The edge cases are covered, the TODO is honest, and this code will still be here long after we're not."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
