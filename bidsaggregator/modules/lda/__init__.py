"""
Module converting LDA CSV output
"""
from utils.module import Module
from .models import Topic, Vertex
import csv

class LDAModule(Module):
    """Module accepting LDA output"""

    meta = {
        'preprocess': 'csv'
    }

    def parse(self, args):
        """Parse input and feed into Graph abstraction outputs"""

        with open(args.csv, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                topics = [s.strip() for s in row.split(',')]
