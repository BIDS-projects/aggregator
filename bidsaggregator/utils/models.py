"""
Database Models
---
BIDS Institutional Ecosystem Mapping

This is the standard structure for all BIDS IEM data. All maps will at
minimum contain information about the following.
"""

class MySQLBase(sad.declarative_base(), object):
    """MySQL base object"""

    __abstract__ = True
    db = None

    id = sa.Column(sa.Integer, primary_key=True)
    updated_at = sa.Column(ArrowType)
    updated_by = sa.Column(sa.Integer)
    created_at = sa.Column(ArrowType, default=arrow.now('US/Pacific'))
    created_by = sa.Column(sa.Integer)
    is_active = sa.Column(sa.Boolean, default=True)

    @classmethod
    def __query(cls):
        """Returns query object"""
        return cls.sa.session.query(cls)

    def save(self):
        """save object to database"""
        self.sa.session.add(self)
        self.sa.session.commit()
        return self


def Graph(Base):
    """abstract for a graph"""

    __tablename__ = 'graph'

    vertices = sa.relationship('Vertex', backref='graph')
    edges = sa.relationship('Edge', backref='graph')


def Vertex(Base):
    """abstract for a graph vertex"""

    __abstract__ = True

    key = sa.Column(sa.String(50), unique=True)
    value = sa.Column(sa.Text)
    graph_id = sa.Column(sa.Integer, sa.ForeignKey('graph.id'))


def Edge(Base):
    """abstract for a graph edge"""

    __abstract__ = True

    value = sa.Column(sa.String)
    graph_id = sa.Column(sa.Integer, sa.ForeignKey('graph.id'))
    from_id = sa.Column(sa.Integer, sa.ForeignKey('vertex.id'))
    to_id = sa.Column(sa.Integer, sa.ForeignKey('vertex.id'))
