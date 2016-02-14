"""
Database Models
---
BIDS Institutional Ecosystem Mapping

This is the standard structure for all BIDS IEM data. All maps will at
minimum contain information about the following.
"""

import sqlalchemy.ext.declarative as sad
from sqlalchemy.orm import relationship
from sqlalchemy import *
from sqlalchemy_utils import ArrowType
import arrow


class Base(sad.declarative_base(), object):
    """MySQL base object"""

    __abstract__ = True
    db = None

    id = Column(Integer, primary_key=True)
    updated_at = Column(ArrowType)
    updated_by = Column(Integer)
    created_at = Column(ArrowType, default=arrow.now('US/Pacific'))
    created_by = Column(Integer)
    is_active = Column(Boolean, default=True)

    @classmethod
    def get_or_create(cls, **data):
        """Get or create the object"""
        return cls.query().filter_by(**data).one_or_none() or cls(**data)

    @classmethod
    def __query(cls):
        """Returns query object"""
        return cls.session.query(cls)

    def add(self):
        """save object to database"""
        self.session.add(self)
        return self

    def save(self):
        """save object to database"""
        self.session.add(self)
        self.session.commit()
        return self


declaredWrap = lambda f: sad.declared_attr(lambda _: f)


##########
# MODELS #
##########


class Graph(Base):
    """abstract for a graph"""

    __tablename__ = 'graph'

    directed = Column(Boolean)
    vertices = relationship('Vertex', backref='graph')
    edges = relationship('Edge', backref='graph')


class Vertex(Base):
    """abstract for a graph vertex"""

    __abstract__ = True

    name = Column(String(50), unique=True)
    value = Column(Text)
    graph_id = declaredWrap(Column(Integer, ForeignKey('graph.id')))


class Edge(Base):
    """abstract for a graph edge"""

    __abstract__ = True

    value = Column(String)

    graph_id = declaredWrap(Column(Integer, ForeignKey('graph.id')))
    from_id = declaredWrap(Column(Integer, ForeignKey('vertex.id')))
    to_id = declaredWrap(Column(Integer, ForeignKey('vertex.id')))
