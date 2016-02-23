"""
Link Weighting Algorithm
---

Weights all edges between websites with a naiive approach
"""
from utils.module import Module
from modules.models import Edge
import csv

class LWAModule(Module):
    """Module accepting raw scraper output"""

    def load(self):
        self.graph.vertices = Vertex.query.all()

    def parse(self, _):
        """
        Weight all edges naiively
        - Query edges by meta-nodes, where each meta-node is a domain
        - Sum up number of edges for a simple graph
        """
        for v in self.graph.vertices:
            Edge.query.join(Vertex).filter(
                Vertex.domain == v.domain,

            )

    def save(self):
        """Save all objects"""
        self.graph.save()
        Vertex.db.session.commit()
