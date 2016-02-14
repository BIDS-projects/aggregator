"""
Module converting LDA CSV output
"""
from utils.module import Module
from utils.models import Vertex, Edge

class LDAModule(Module):
    """Module accepting LDA output"""

    def parse(self, input):
        """Parse input and feed into Graph abstraction outputs"""
