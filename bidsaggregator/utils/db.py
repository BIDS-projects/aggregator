from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database(object):
    """Database object for database connections"""

    def __init__(self, string=None):
        self.agg_engine = create_engine(
            string or 'mysql+pymysql://root:root@localhost/aggregator')
        self.Session = sessionmaker(bind=agg_engine)
        self.session = self.Session()


db = Database()
