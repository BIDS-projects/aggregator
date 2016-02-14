from utils.models import Vertex as V, Base
import sqlalchemy as sa


def Vertex(V):
    """lda vertex abstract"""

    __tablename__ = 'vertex'

    topics = sa.relatioship('Topic', backref='vertex')


def Topic(Base):

    __tablename__ = 'topic'

    parent_id = sa.Column(sa.Integer, sa.PrivateKey('topic.id'))
    vertex_id = sa.Column(sa.Integer, sa.ForeignKey('vertex.id'))
