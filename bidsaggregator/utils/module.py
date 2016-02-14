"""
Default module
"""

from utils.models import Graph

class Module(object):
    """base module object - defines contract for all modules"""

    graph = None
    vertices = ()
    edges = ()

    def __init__(self):
        """setup objects"""
        self.graph = Graph()
        self.vertices = []
        self.edges = []

    def run(self, args):
        """General run procedure"""
        data = self.load(args)
        self.parse(self.preprocess(data))
        return self.save()

    def load(self, args):
        """Load data required to begin processing"""
        raise NotImplementedError()

    def preprocess(self, data):
        """Preprocess input and feed into parse"""
        return data

    def parse(self, data):
        """Parse input and feed into Graph abstraction outputs"""
        raise NotImplementedError()

    def save(self, input):
        """Save all objects to the db"""
        self.graph.save()
        for vertex in self.vertices:
            vertex.save()
        for edge in edges:
            edge.save()
