import pytest

import sys

sys.path.append('bidsaggregator')

from modules.lda import LDAModule
from unittest.mock import MagicMock


def test_load():
    """test that loading from CSV works"""
    filepath = 'tests/data/bids.csv'
    filedata = 'data,keyword1,keyword2,keyword3,keyword4,keyword5,keyword6,keyword7,keyword8,keyword8,keyword9,keyword10'

    f = open(filepath, 'w')
    f.write(filedata)
    f.close()

    data = LDAModule().load(MagicMock(csv=filepath))
    assert data['institution'] == 'bids'
    assert data['topics'][0][0] == 'data'
    assert data['topics'][0][1] == filedata.split(',')[1:]


def test_parse():
    """Tests that LDA parsed correctly"""
    
