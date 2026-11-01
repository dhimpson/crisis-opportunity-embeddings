#!/usr/bin/env python3
"""
Step 0a: Download The Crisis and Opportunity from the Internet Archive
======================================================================

Finds every issue of the two magazines on archive.org between FIRST_YEAR
and LAST_YEAR and downloads only the OCR text of each one (the
"_djvu.txt" file), not the scans. Each issue is saved as

    corpus-raw/<magazine>/<MAGAZINE>_<year>_<month>.txt

Uses only Python's built-in libraries, so nothing extra to install.
Run it again if it stops partway: issues you already have are skipped.

Some issues on archive.org are borrow-only and can't be downloaded; the
script reports how many it skipped.

Why stop at 1930? Magazines published in 1930 or earlier are in the US
public domain (as of 2026). Later issues may still be under copyright.
"""

import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

# --- Settings ------------------------------------------------------------------

FIRST_YEAR = 1910
LAST_YEAR = 1930

# Each magazine: its folder name, and the archive.org search that finds its issues.
# The issue identifiers look like sim_crisis_1910-11_1_1 (year-month_volume_issue).
MAGAZINES = {
    "crisis": {
        "query": "collection:pub_crisis OR identifier:sim_crisis_*",
        "prefix": "sim_crisis_",
    },
    "opportunity": {
        "query": "collection:pub_opportunity-a-journal-of-negro-life "
                 "OR identifier:sim_opportunity-a-journal-of-negro-life_*",
        "prefix": "sim_opportunity-a-journal-of-negro-life_",
    },
}

PAUSE = 1.0     # seconds to wait between downloads, to be polite to archive.org

# -------------------------------------------------------------------------------

RAW_FOLDER = SCRIPT_DIR / "corpus-raw"
HEADERS = {"User-Agent": "8510 class word-embedding corpus download (Python)"}

# year and month from an identifier like sim_crisis_1910-11_1_1
ISSUE_DATE = re.compile(r"_(\d{4})-(\d{2})")


def get(url, retries=4):
    """Fetch a URL, trying again a few times if the connection fails."""
    for attempt in range(retries):
        try:
            request = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(request, timeout=60) as response:
                return response.read()
        except urllib.error.HTTPError as error:
            if error.code in (401, 403, 404):      # restricted or missing: don't retry
                raise
            time.sleep(5 * (attempt + 1))
        except (urllib.error.URLError, TimeoutError):
            time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"couldn't reach {url}")


def find_issues(query, prefix):
    """Search archive.org and return {(year, month): [identifiers]}."""
    params = urllib.parse.urlencode(
        {"q": query, "fl[]": "identifier", "rows": 5000, "output": "json"})
    data = json.loads(get(f"https://archive.org/advancedsearch.php?{params}"))
    issues = {}
    for doc in data["response"]["docs"]:
        identifier = doc["identifier"]
        match = ISSUE_DATE.search(identifier)
        if not identifier.startswith(prefix) or not match:
            continue
        year, month = int(match.group(1)), int(match.group(2))
        if FIRST_YEAR <= year <= LAST_YEAR:
            issues.setdefault((year, month), []).append(identifier)
    return issues


def text_file_name(identifier):
    """Look up the name of the item's OCR text file (it ends in _djvu.txt)."""
    metadata = json.loads(get(f"https://archive.org/metadata/{identifier}"))
    for file in metadata.get("files", []):
        if file["name"].endswith("_djvu.txt"):
            return file["name"]
    return None


def download_issue(identifier, out_path):
    """Download one issue's OCR text. Returns True if it worked."""
    name = text_file_name(identifier)
    if name is None:
        return False
    url = f"https://archive.org/download/{identifier}/{urllib.parse.quote(name)}"
    text = get(url).decode("utf-8", errors="replace")
    out_path.write_text(text, encoding="utf-8")
    return True


def main():
    for magazine, settings in MAGAZINES.items():
        folder = RAW_FOLDER / magazine
        folder.mkdir(parents=True, exist_ok=True)

        print(f"\nSearching archive.org for {magazine} ...")
        issues = find_issues(settings["query"], settings["prefix"])
        print(f"  found {len(issues)} issues, {FIRST_YEAR}-{LAST_YEAR}")

        got, skipped, failed = 0, 0, []
        for (year, month), identifiers in sorted(issues.items()):
            out_path = folder / f"{magazine.upper()}_{year}_{month:02d}.txt"
            if out_path.exists():
                skipped += 1
                continue
            # If an issue was scanned more than once, use the first copy that downloads
            for identifier in identifiers:
                try:
                    if download_issue(identifier, out_path):
                        got += 1
                        print(f"  {out_path.name}  <- {identifier}")
                        break
                except Exception:                   # borrow-only, missing, etc.
                    pass
                time.sleep(PAUSE)
            else:
                failed.append(f"{year}-{month:02d}")
            time.sleep(PAUSE)

        print(f"  {magazine}: downloaded {got}, already had {skipped}, "
              f"couldn't get {len(failed)}")
        if failed:
            print(f"  couldn't get: {', '.join(failed)}")

    print("\nDone. Next: python 00b_clean_corpus.py")


if __name__ == "__main__":
    main()
