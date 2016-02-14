"""
Module converting LDA CSV output
"""
from utils.module import Module
from .models import Topic, Vertex, Keyword, KeywordTopic, TopicVertex
import csv

class LDAModule(Module):
    """Module accepting LDA output"""

    def load(self, args):
        """Load CSV file"""
        topics = []
        with open(args.csv, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                topics.append((row[0], row[1:]))
        return {
            'institution': args.csv.split('.')[-2].split('/')[-1].strip(),
            'topics': topics
        }

    def parse(self, data):
        """Convert CSV topics into vertices and topics"""
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
