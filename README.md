# Word Embeddings: *The Crisis* and *Opportunity*, 1910–1930

Train word2vec models on two Black periodicals: *The Crisis* (NAACP, edited by
W. E. B. Du Bois, 1910–) and *Opportunity: A Journal of Negro Life* (National Urban
League, 1923–). Explore what the models learned, then align models from different
periods to see how words changed meaning across the 1910s and 1920s.

Research Question: How does *The Crisis* and *Opportunity* document segregation and racial residential segregation ordinances in the first thirty years of the twentieth century?

Adapted from the 8510 Week 10 word-embeddings tutorial; scripts 01–05 work the same way.

| Script | What it does | What you change |
|---|---|---|
| `00a_download_corpus.py` | Downloads the OCR text of every issue, 1910–1930, from the Internet Archive | `FIRST_YEAR`, `LAST_YEAR` |
| `00b_clean_corpus.py` | Cleans the OCR and sorts issues into period folders | `PERIODS`, `SOURCES` |
| `01_train_model.py` | Trains a model on one folder of text | `CORPUS_FOLDER`, `MODEL_NAME` |
| `02_explore_model.py` | Nearest words, nearest to several words, a 2D plot of a word and its neighbors | `MODEL_NAME`, `WORD`, `SEED_WORDS`, `PLOT_COUNT` |
| `03_align_models.py` | Aligns the period models so they can be compared | (nothing, unless you rename models) |
| `04_explore_change.py` | Traces one word across the periods | `WORD` |
| `05_gender_and_a_word.py` | Which words near a target word lean toward women, and which toward men (after Schmidt) | `MODEL_NAME`, `TARGET`, `WOMEN_WORDS`, `MEN_WORDS` |

---

## Setup

### Step 1: Python 3.13

gensim doesn't work with Python 3.14 yet, so use **Python 3.13** (as in Week 10).

```bash
python3.13 --version            # Mac
py -3.13 --version              # Windows
```

If it's missing: `brew install python@3.13` (Mac with Homebrew), or the 3.13 installer from
<https://www.python.org/downloads/>.

### Step 2: Create the virtual environment

From inside the `crisis-opportunity-embeddings` folder:

```bash
python3.13 -m venv venv         # Windows: py -3.13 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
python --version                # should say Python 3.13.x
pip install -r requirements.txt
```

### Step 3: Download the corpus

```bash
python 00a_download_corpus.py
```

This searches archive.org and downloads only the OCR text of each issue (no scans), about
a second per issue, so expect 10–15 minutes for roughly 330 issues. If it stops partway,
run it again; it skips issues you already have. A few issues may be borrow-only on
archive.org; the script lists the ones it couldn't get.

You'll have:

```
corpus-raw/
├── crisis/          CRISIS_1910_11.txt, CRISIS_1910_12.txt, ...
└── opportunity/     OPPORTUNITY_1923_01.txt, ...
```

### Step 4: Clean the text and sort it into periods

```bash
python 00b_clean_corpus.py
```

It prints the number of issues and words in each period. You should see several million
words in total.

```
corpus-clean/
├── 1910-1916/
├── 1917-1923/
└── 1924-1930/
```

---

## Running it

```bash
source venv/bin/activate        # Windows: venv\Scripts\activate
```

**1. Train three models,** one per period. Run `01_train_model.py` three times, changing these
two lines at the top each time:

```python
CORPUS_FOLDER = SCRIPT_DIR / "corpus-clean" / "1910-1916"
MODEL_NAME = "1910-1916"
```

```bash
python 01_train_model.py
```

**2. Explore a model:** `python 02_explore_model.py`

**3. Align the three models:** `python 03_align_models.py`

**4. Trace a word over time:** `python 04_explore_change.py`

**5. Gender and a word:** `python 05_gender_and_a_word.py`

Plots are saved in `plots/` and open automatically.

While training you may see `Exception ignored in: 'gensim.models.word2vec_inner.our_dot_float'`.
It's a known, harmless gensim bug ([issue #3665](https://github.com/piskvorky/gensim/issues/3665)).

---

## Things to keep in mind

- **The periods aren't balanced.** *Opportunity* starts in 1923, so 1910–1916 is *The Crisis*
  alone, and 1924–1930 has both magazines. Some differences between periods will come from
  the mix of sources, not just change over time. To compare like with like, set
  `SOURCES = ["crisis"]` in `00b_clean_corpus.py` and rerun steps 4 and 1–4.
- **OCR errors become "words,"** and the cleaning doesn't remove advertisements. Expect
  fragments and ad vocabulary among the neighbors.
- **Results change a little every time you train,** even with the same settings.
- **The language is the sources' own.** Expect the period's terms ("Negro," "colored") as
  the most frequent words for people, and offensive terms quoted in reporting on racism.

## Rights

Both magazines' issues from 1930 and earlier are in the US public domain. The text comes
from the Internet Archive's scans (collections `pub_crisis` and
`pub_opportunity-a-journal-of-negro-life`). The downloaded and cleaned text is left out of
git (see `.gitignore`); anyone can rebuild it with steps 3 and 4.
