from utils.models import Vertex as V, Edge as E, Base, declaredWrap
from sqlalchemy import *


class Edge(E):
    """lda edge abstract"""

    __tablename__ = 'edge'
    

class Vertex(V):
    """lda vertex abstract"""

    __tablename__ = 'vertex'


class TopicVertex(Base):

    __tablename__ = 'topic_vertex'

    topic_id = declaredWrap(Column(Integer, ForeignKey('topic.id')))
    vertex_id = declaredWrap(Column(Integer, ForeignKey('vertex.id')))


class Keyword(Base):

    __tablename__ = 'keyword'

    name = Column(String(50), unique=True)


class KeywordTopic(Base):

    __tablename__ = 'keyword_topic'
    topic_id = declaredWrap(Column(Integer, ForeignKey('topic.id')))
    keyword_id = declaredWrap(Column(Integer, ForeignKey('keyword.id')))


class Topic(Base):

    __tablename__ = 'topic'

    name = Column(String(50), unique=True)
