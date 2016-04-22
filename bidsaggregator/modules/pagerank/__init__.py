"""
Module for Page Rank
"""
from utils.module import Module
from modules.lda.models import Topic, Edge, Keyword, KeywordTopic, TopicVertex
from db import MySQL, MySQLConfig, FromItem, ToItem, Institution
from sqlalchemy import func, distinct, select, create_engine
import csv



class PageRankModule(Module):
    """Module accepting LDA output"""

    def load(self, args):
        mysql = MySQL(config=MySQLConfig)

    def parse(self, data):
        """
        Pseudocode to query links for edges.
        """
        with open('institutions.csv', 'rt') as f:
            reader = csv.reader(f)
            institutions = list(reader)
            for i in range(len(institutions)):
                institution = bytes(institutions[i][0], 'utf-8')
                institutions[i] = institution

        engine = create_engine('mysql+pymysql://user:password@localhost/ecosystem_mapping')
        conn = engine.connect()
        s = select([ToItem.id,
            ToItem.from_id, 
            ToItem.base_url, 
            FromItem.base_url, 
            func.count(ToItem.base_url)]).where(
            ToItem.base_url != bytes('', 'utf-8')).where( 
            ToItem.base_url != bytes("berkeley.edu", 'utf-8')).where(
            ToItem.from_id == FromItem.id).group_by(ToItem.base_url).order_by(
            FromItem.base_url)

        for row in conn.execute(s):
            for institution in institutions:
                if row[2] in institution:
                    edge = Edge.get_or_create(
                        # graph_id = 1,
                        to_id = row[0],
                        from_id = row[1],
                        to_domain = row[2],
                        from_domain = row[3],
                        value = row[4])
                    self.edges.append(edge)

    def save(self):
        """Save all objects"""
        self.graph.save()
        Edge.db.session.commit()