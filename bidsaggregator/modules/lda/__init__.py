"""
Module converting LDA CSV output
"""
from utils.module import Module
from .models import Topic, Vertex, Keyword, KeywordTopic, TopicVertex
import csv

class LDAModule(Module):
    """Module accepting LDA output"""

    artifacts = []

    def load(self, args):
        """Load CSV file"""
        topics = []
        with open(args.csv, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                words = [s.strip() for s in row.split(',')]
                topics.append((words[0], words[1:]))
        return {
            'institution': args.csv.split('.')[0].strip(),
            'topics': topics
        }

    def parse(self, data):
        """Convert CSV topics into vertices and topics"""
        vertex = Vertex.get_or_create(name=data['institution'])
        for topic, keywords in data['topics']:
            topic = Topic.get_or_create(name=topic)
            tv = TopicVertex.get_or_create(
                topic_id=topic.id, vertex_id=vertex.id)
            for keyword in keywords:
                kw = Keyword.get_or_create(name=keyword)
                kt = KeywordTopic.get_or_create(
                    keyword_id=keyword.id, topic_id=topic.id)
                artifacts.extend([kw, kt])
            artifacts.extend([topic, tv])
        self.vertices.append(vertex)

    def save(self):
        """Save all objects"""
        self.graph.save()
        for vertex in self.vertices:
            vertex.add()
        for artifact in artifacts:
            artifact.add()
        Vertex.db.session.commit()
