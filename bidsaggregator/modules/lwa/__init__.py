"""
Link Weighting Algorithm
---

Weights all edges between websites with a naiive approach
"""
from utils.module import Module
from modules.models import Edge
from .models import Link, HTML
import csv


class LWAModule(Module):
    """Module accepting raw scraper output"""

    def load(self):
        self.graph.vertices = Vertex.query.all()

    def parse(self, _):
        """
        Weight all edges naiively
        - Query edges by meta-nodes, where each meta-node is a domain
        - Create new edges between meta-nodes where the "weight" is the number
          of multi-edges in the associated multi-graph.
        """
        for v in self.graph.vertices:
            for u in self.graph.vertices:
                weight = Link.query.join(HTML).filter(
                    HTML.domain == v.domain).count()
                edge = Edge.get_or_create(
                    graph_id=self.graph.id,
                    from_id=u.id,
                    to_id=v.id)
                if not edge:
                    Edge(graph_id=self.graph.id,
                        from_id=u.id,
                        to_id=v.id,
                        weight=weight).save()
                else:
                    edge.weight = weight
                    edge.save()


    def save(self):
        """Save all objects"""
        self.graph.save()
        Vertex.db.session.commit()
