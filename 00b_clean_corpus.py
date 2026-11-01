#!/usr/bin/env python3
"""
Step 0b: Clean the OCR text and sort it into periods
====================================================

Reads the raw issues in corpus-raw/, cleans up the most common OCR
problems, and saves each issue into one folder per period:

    corpus-clean/1910-1916/CRISIS_1912_May.txt
    corpus-clean/1917-1923/OPPORTUNITY_1923_January.txt
    corpus-clean/1924-1930/...

What the cleaning does:
  - rejoins words split across a line break ("Neg-\\nroes" -> "Negroes")
  - drops lines that are mostly numbers or symbols (page numbers, table
    rows, scanning noise) and very short fragments
  - drops the magazines' running heads ("THE CRISIS", "OPPORTUNITY")
  - joins the lines of each paragraph back into one line, keeping a
    blank line between paragraphs (01_train_model.py splits on those)

It does NOT remove advertisements or fix misspelled OCR words. Those will
still show up in the models.

Change PERIODS to split the years differently, or SOURCES to use only
one magazine. Run it again after any change: it rebuilds corpus-clean/.
"""

import re
import shutil
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

# --- Settings ------------------------------------------------------------------

# Each period: folder name -> (first year, last year)
PERIODS = {
    "1910-1916": (1910, 1916),
    "1917-1923": (1917, 1923),
    "1924-1930": (1924, 1930),
}

SOURCES = ["crisis", "opportunity"]     # which folders in corpus-raw/ to use

MIN_LETTER_SHARE = 0.6   # drop a line if less than 60% of its characters are letters
MIN_LINE_LENGTH = 4      # drop lines shorter than this (stray characters)

# -------------------------------------------------------------------------------

RAW_FOLDER = SCRIPT_DIR / "corpus-raw"
CLEAN_FOLDER = SCRIPT_DIR / "corpus-clean"

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
FILE_NAME = re.compile(r"([A-Z]+)_(\d{4})_(\d{2})\.txt")
RUNNING_HEAD = re.compile(r"^(THE\s+)?(CRISIS|OPPORTUNITY)\b[\W\d]*$", re.IGNORECASE)
WORD = re.compile(r"[a-z]+(?:['-][a-z]+)*")


def keep_line(line):
    """False for page numbers, running heads, table rows and scanning noise."""
    stripped = line.strip()
    if len(stripped) < MIN_LINE_LENGTH or RUNNING_HEAD.match(stripped):
        return False
    letters = sum(c.isalpha() for c in stripped)
    visible = sum(not c.isspace() for c in stripped)
    return letters / visible >= MIN_LETTER_SHARE


def clean(text):
    text = text.replace("\r\n", "\n").replace("﻿", "")
    text = text.replace("­", "")                        # invisible soft hyphens
    text = re.sub(r"[‘’]", "'", text)              # curly quotes -> straight
    text = re.sub(r"[“”]", '"', text)
    text = re.sub(r"(\w)[-‐‑¬]\s*\n\s*(\w)", r"\1\2", text)   # rejoin split words
    text = re.sub(r"\f", "\n\n", text)                       # page breaks end a paragraph

    paragraphs = []
    for block in re.split(r"\n\s*\n", text):
        lines = [l.strip() for l in block.split("\n") if keep_line(l)]
        if lines:
            paragraphs.append(re.sub(r"\s+", " ", " ".join(lines)))
    return "\n\n".join(paragraphs) + "\n"


def period_for(year):
    for name, (first, last) in PERIODS.items():
        if first <= year <= last:
            return name
    return None


def main():
    if not RAW_FOLDER.exists():
        print("Can't find corpus-raw/. Run 00a_download_corpus.py first.")
        return

    if CLEAN_FOLDER.exists():
        shutil.rmtree(CLEAN_FOLDER)
    totals = {name: [0, 0] for name in PERIODS}               # files, words

    for source in SOURCES:
        for path in sorted((RAW_FOLDER / source).glob("*.txt")):
            match = FILE_NAME.fullmatch(path.name)
            if not match:
                continue
            magazine, year, month = match.group(1), int(match.group(2)), int(match.group(3))
            period = period_for(year)
            if period is None:
                continue
            cleaned = clean(path.read_text(encoding="utf-8", errors="replace"))
            out = CLEAN_FOLDER / period / f"{magazine}_{year}_{MONTHS[month - 1]}.txt"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(cleaned, encoding="utf-8")
            totals[period][0] += 1
            totals[period][1] += len(WORD.findall(cleaned.lower()))

    print("Cleaned corpus:")
    for name, (files, words) in totals.items():
        print(f"  corpus-clean/{name}:  {files:4} issues  {words:>12,} words")
    print(f"  {'total':>22}  {sum(f for f, _ in totals.values()):4} issues  "
          f"{sum(w for _, w in totals.values()):>12,} words")
    print("\nNext: python 01_train_model.py")


if __name__ == "__main__":
    main()
