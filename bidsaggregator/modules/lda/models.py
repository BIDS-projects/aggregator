from utils.models import Vertex as V, Base
from sqlalchemy import *


class Vertex(V):
    """lda vertex abstract"""

    __tablename__ = 'vertex'


class TopicVertex(Base):

    __table__ = 'topic_vertex'

    topic_id = Column(Integer, ForeignKey('topic.id'))
    vertex_id = Column(Integer, ForeignKey('vertex.id'))


class Keyword(Base):

    __tablename__ = 'keyword'

    name = Column(String(50), unique=True)


class KeywordTopic(Base):

    __table__ = 'keyword_topic'

    topic_id = Column(Integer, ForeignKey('topic.id'))
    keyword_id = Column(Integer, ForeignKey('keyword.id'))


class Topic(Base):

    __tablename__ = 'topic'

    name = Column(String(50), unique=True)
