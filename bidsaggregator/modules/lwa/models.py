"""
Database Models
---
BIDS Institutional Ecosystem Mapping
"""

from utils.models import Base, ForeignColumn
import sqlalchemy as sa


class HTML(Base):
    """webpage"""

    __tablename__ = 'html'

    domain = sa.Column(sa.Text)
    url = sa.Column(sa.Text)
    body = sa.Column(sa.String(50))
    request = sa.Column(sa.Text)


class Link(Base):
    """link between webpages"""

    __tablename__ = 'link'

    from_html = ForeignColumn(Integer, ForeignKey('html.id'))
    to_html = ForeignColumn(Integer, ForeignKey('html.id'))
