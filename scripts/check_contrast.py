#!/usr/bin/env python3
"""Check the documented palette against the contrast minimums on a white page.

Reads the color tables in rules/typography-and-color.md and verifies:
  - text colors reach 4.5:1 against white
  - data colors reach 3:1 against white
The page, gridline and field rows are skipped. Rows whose use says "Not for marks"
or "Avoid" are reported but never fail: the file already restricts them.

Usage: python3 scripts/check_contrast.py    (exit code 1 on any failure)
No dependencies beyond the Python standard library.
"""

import re
import sys
from pathlib import Path

DOC = Path(__file__).resolve().parent.parent / "rules" / "typography-and-color.md"
PAGE = "#ffffff"
TEXT_MIN, DATA_MIN = 4.5, 3.0
HEX = re.compile(r"#[0-9a-fA-F]{6}\b")


def luminance(hex_color):
    channels = []
    for i in (1, 3, 5):
        c = int(hex_color[i:i + 2], 16) / 255
        channels.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    r, g, b = channels
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def table_rows(text, heading):
    """Rows (as lists of cells) of the first table under a '### heading'."""
    rows, inside = [], False
    for line in text.splitlines():
        if line.startswith("#"):
            if inside and rows:
                break
            inside = line.lstrip("#").strip() == heading
            continue
        if inside and line.startswith("|") and not re.match(r"^\|[\s\-|]+\|$", line):
            rows.append([c.strip().strip("`") for c in line.strip("|").split("|")])
    return rows[1:]  # drop the header row


def main():
    text = DOC.read_text(encoding="utf-8")
    checks = []  # (label, color, minimum, may_fail)

    for role, color, *_ in table_rows(text, "Page, text and axes"):
        name = role.lower()
        if name == "page" or "grid" in name:
            continue
        minimum = TEXT_MIN if name.startswith("text") else DATA_MIN
        checks.append((role, color, minimum, True))

    for role, color, _ratio, use in table_rows(text, "Tufte's palette: black and grays, one accent, muted fields"):
        if "field" in role.lower():
            continue
        minimum = TEXT_MIN if "label may share its color" in use else DATA_MIN
        checks.append((role, color, minimum, True))

    for name, color, _ratio, use in table_rows(text, "Fallback for several categories: Okabe–Ito"):
        restricted = "not for marks" in use.lower() or use.strip().lower() == "avoid"
        minimum = TEXT_MIN if "label may share its color" in use else DATA_MIN
        checks.append((f"Okabe–Ito {name}", color, minimum, not restricted))

    if not checks:
        print("error: no color tables found in", DOC)
        return 1

    failures = 0
    for label, color, minimum, may_fail in checks:
        if not HEX.fullmatch(color):
            print(f"skip  {label}: '{color}' is not a hex color")
            continue
        ratio = contrast(color, PAGE)
        ok = ratio >= minimum
        if ok:
            status = "ok  "
        elif may_fail:
            status, failures = "FAIL", failures + 1
        else:
            status = "info"
        print(f"{status}  {ratio:5.2f}:1 (needs {minimum}:1)  {color}  {label}")

    print(f"\n{len(checks)} checks, {failures} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
