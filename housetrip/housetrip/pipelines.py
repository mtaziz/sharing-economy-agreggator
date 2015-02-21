#! -*- coding: utf-8 -*-

"""
Web Scraper Project

Scrape data from a regularly updated website drivy.com and
save to a database (postgres).

Scrapy pipeline part - stores scraped items in the database.
"""

from sqlalchemy.orm import sessionmaker
from models import HousetripDeals, db_connect, create_housetripdeals_table


class HousetripPipeline(object):
    """housetrip pipeline for storing scraped items in the database"""
    def __init__(self):
        """Initializes database connection and sessionmaker.

        Creates housetrip deals table.

        """
        engine = db_connect()
        create_housetripdeals_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save housetrip deals in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        deal = HousetripDeals(**item)

        try:
            session.add(deal)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item