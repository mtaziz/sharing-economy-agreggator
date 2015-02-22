#! -*- coding: utf-8 -*-

"""
Web Scraper Project

Scrape data from a regularly updated website jestocke.com and
save to a database (postgres).

Scrapy pipeline part - stores scraped items in the database.
"""

from sqlalchemy.orm import sessionmaker
from models import JestockeDeals, db_connect, create_jestockedeals_table


class JestockePipeline(object):
    """jestocke pipeline for storing scraped items in the database"""
    def __init__(self):
        """Initializes database connection and sessionmaker.

        Creates jestocke deals table.

        """
        engine = db_connect()
        create_jestockedeals_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save jestocke deals in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        deal = JestockeDeals(**item)

        try:
            session.add(deal)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item