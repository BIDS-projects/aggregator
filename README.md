# Aggregator
Aggregates processed data in any form, converts all into Graph abstracts.

# Installation

If you intend on using the aggregator's CLI, clone the repository.

```
git clone git@github.com:BIDS-projects/aggregator.git
```

If you intend on using this package programmatically, install via `pip` directly via Github.

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
python aggregator.py lda --csv=path/to/[institution].csv
```

The `[institution]` portion is the name of the institution, as stored in the
database. Use `_` instead of spaces.

## Link Weighting Algorithm (LWA)

A rather naiive algorithm that reduces a multigraph to a simple graph, by summing the number of edges between meta-nodes, where each node is a domain. This then becomes a new edge weight between two vertices. To process raw scraper output, run the following.

```
python aggregator.py lwa
```
