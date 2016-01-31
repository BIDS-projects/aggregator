"""
Default module
"""

from utils.models import Graph, Vertex, Edge

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

    def parse(self, input):
        """Parse input and feed into Graph abstraction outputs"""
        raise NotImplementedError()

    def save(self, input):
        """Save all objects to the db"""
        self.graph.save()
        for vertex in self.vertices:
            vertex.save()
        for edge in edges:
            edge.save()
