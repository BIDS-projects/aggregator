"""
Module for Page Rank
"""
from utils.module import Module
from modules.lda.models import Topic, Vertex, Keyword, KeywordTopic, TopicVertex
import csv

class PageRankModule(Module):
    """Module accepting LDA output"""

    def load(self, args):
        pass

    def parse(self, data):
        """Waiting on output of json file."""
        vertex = Vertex.get_or_create(
            name=data['institution'],
            graph_id=self.graph.id)
        for topic, keywords in data['topics']:
            topic = Topic.get_or_create(name=topic)
            tv = TopicVertex.get_or_create(
                topic_id=topic.id, vertex_id=vertex.id)
            for keyword in keywords:
                kw = Keyword.get_or_create(name=keyword)
                kt = KeywordTopic.get_or_create(
                    keyword_id=kw.id, topic_id=topic.id)
        self.vertices.append(vertex)

    def save(self):
        """Save all objects"""
        self.graph.save()
        Vertex.db.session.commit()