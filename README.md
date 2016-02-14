# Aggregator
Aggregates processed data in any form, converts all into Graph abstracts.

# Installation

```
pip install git+https://github.com/BIDS-projects/aggregator.git
```

# How to Use

```
python aggregator.py [analysis]
```

## LDA

To process a CSV generated from LDA, run the following:

```
python aggregator.py lda --csv=[institution].csv
```

The `[institution]` portion is the name of the institution, as stored in the
database. Use `_` instead of spaces.
