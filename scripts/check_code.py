#!/usr/bin/env python3
"""Run the Python code in rules/matplotlib.md and the example scripts.

Every ```python block in rules/matplotlib.md is executed in order, in one
namespace, inside a temporary directory, so the file's examples must run as
written. Then each script in examples/ is run with a temporary output folder.

Usage: python3 scripts/check_code.py    (exit code 1 on any failure)
Needs matplotlib, NumPy, SciPy, pandas and seaborn.
"""

import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RULES = ROOT / "rules" / "matplotlib.md"
BLOCK = re.compile(r"```python\n(.*?)```", re.S)


def code_blocks(path):
    return BLOCK.findall(path.read_text(encoding="utf-8"))


def main():
    import matplotlib
    matplotlib.use("Agg")
    import os

    failures = 0
    blocks = code_blocks(RULES)
    with tempfile.TemporaryDirectory() as tmp:
        cwd = os.getcwd()
        os.chdir(tmp)
        namespace = {"__name__": "__check__"}
        try:
            for i, block in enumerate(blocks, 1):
                try:
                    exec(compile(block, f"{RULES.name} block {i}", "exec"), namespace)
                    print(f"ok    {RULES.name} block {i}")
                except Exception as exc:  # report and keep going
                    failures += 1
                    print(f"FAIL  {RULES.name} block {i}: {type(exc).__name__}: {exc}")
        finally:
            os.chdir(cwd)

        scripts = sorted((ROOT / "examples").glob("*.py"))
        for script in scripts:
            out = Path(tmp) / script.stem
            result = subprocess.run([sys.executable, str(script), str(out)],
                                    capture_output=True, text=True)
            if result.returncode == 0:
                print(f"ok    examples/{script.name}")
            else:
                failures += 1
                print(f"FAIL  examples/{script.name}\n{result.stderr.strip()}")

    print(f"\n{len(blocks)} code blocks and {len(scripts)} example scripts checked, {failures} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
