"""
Link Weighting Algorithm
---

Weights all edges between websites with a naiive approach
"""
from utils.module import Module
from models import Edge, Vertex
from .models import Link, HTML
import csv


class LWAModule(Module):
    """Module accepting raw scraper output"""

    def load(self, args):
        """Load all domains from scraper into new graph"""
        domains = set(h.domain for h in HTML.query().all())
        for domain in domains:
            Vertex.get_or_create(domain=domain).save()
        self.graph.vertices = Vertex.query().all()

    def parse(self, _):
        """
        Weight all edges naiively
        - Query edges by meta-nodes, where each meta-node is a domain
        - Create new edges between meta-nodes where the "weight" is the number
          of multi-edges in the associated multi-graph.
        """
        for v in self.graph.vertices:
            print('Computing edge weights for "%s"' % v.domain)
            for u in self.graph.vertices:
                weight = Link.query().join(
                    HTML, Link.from_html==HTML.id).filter(
                    HTML.domain == u.domain).count()
                # print('Edge (%s, %s): %d' % (v.domain, u.domain, weight))
                edge = Edge.get_or_create(
                    graph_id=self.graph.id,
                    from_id=u.id,
                    to_id=v.id).update(weight=weight).save()


    def save(self):
        """Save all objects"""
        self.graph.save()
        Vertex.db.session.commit()
