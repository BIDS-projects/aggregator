from utils.models import Vertex as V, Edge as E, Base, ForeignColumn
from sqlalchemy import *


class Edge(E):
    """lda edge abstract"""

    __tablename__ = 'edge'

    weight = Column(Integer)


class Vertex(V):
    """lda vertex abstract"""

    __tablename__ = 'vertex'

    domain = Column(Text)


class TopicVertex(Base):

    __tablename__ = 'topic_vertex'

    topic_id = ForeignColumn(Integer, ForeignKey('topic.id'))
    vertex_id = ForeignColumn(Integer, ForeignKey('vertex.id'))


class Keyword(Base):

    __tablename__ = 'keyword'

    name = Column(String(50), unique=True)


class KeywordTopic(Base):

    __tablename__ = 'keyword_topic'
    topic_id = ForeignColumn(Integer, ForeignKey('topic.id'))
    keyword_id = ForeignColumn(Integer, ForeignKey('keyword.id'))


class Topic(Base):

    __tablename__ = 'topic'

    name = Column(String(50), unique=True)
