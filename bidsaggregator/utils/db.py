from .config import *
from .models import *

import sqlalchemy as sa
import sqlalchemy.orm as sao


class MySQL(object):
    """MySQL database connection abstraction"""

    def __init__(self, config):
        """initialize connection"""
        self.engine = sa.create_engine(
            'mysql+pymysql://{username}:{password}@{host}/{database}'.format(
            username=config.username,
            password=config.password,
            host=config.host,
            database=config.database))
        self.session = sao.scoped_session(sao.sessionmaker(bind=self.engine))

        # set db to self
        MySQLBase.db = self

        # extra MySQL initialization
        MySQLBase.metadata.create_all(bind=self.engine)
