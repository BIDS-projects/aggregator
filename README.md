# Aggregator
Aggregates processed data in any form, converts all into Graph abstracts.

# Installation

Clone the repository.

```
git clone git@github.com:BIDS-projects/aggregator
```

Setup your virtual environment. The following will create a new environment called `aggregator`.

```
conda create -n aggregator python=3.4
```

Activate your virtual environment, and install all dependencies from `requirements.txt`.

```
source activate aggregator
pip install -r requirements.txt
```

Installation complete. See "How to Use" to get started.

# How to Use

Make sure to activate your virtual environment, if you haven't already. (If you are in the environment, your prompt will be prefixed by `(aggregator)`)

```
source activate aggregator
```

To run an aggregation module, use the following, where `analysis` is the name of your analysis. See below for types of analysis output that this aggregator can accept.

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

A rather naiive algorithm that reduces a multigraph to a simple graph, by summing the number of edges between meta-nodes, where each node is a domain. This then becomes a new edge weight between two vertices. To process raw scraper output in MySQL, run the following.

```
python aggregator.py lwa
```

# Deployment

You must have an account on Mercury, setup through BIDS IEM. SSH onto server.

```
ssh [username]@mercury.dlab.berkeley.edu
```

[More instructions coming soon]
