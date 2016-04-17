#! -*- coding: utf-8 -*-

"""
Web Scraper Project

Scrape data from a regularly updated website drivy.fr and
save to a database (postgres).

Database models part - defines table for storing scraped data.
Direct run will create the table.
"""

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings


DeclarativeBase = declarative_base()


def db_connect():
    """Performs database connection using database settings from settings.py.

    Returns sqlalchemy engine instance.

    """
    return create_engine(URL(**settings.DATABASE))


def create_housetripdeals_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class HousetripDeals(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "ads"

    id = Column(Integer, primary_key=True)
    creation_date = Column('creation_date', String, nullable=True) 
    title = Column('title', String)
    media = Column('media', String, nullable=True)
    link = Column('link', String, nullable=True)
    desc = Column('desc', String, nullable=True)
    location = Column('location', String, nullable=True)
    distance = Column('distance', String, nullable=True)
    price = Column('price', String, nullable=True)
    period = Column('period', String, nullable=True)
    source = Column('source', String, nullable=True)
    category = Column('category', String, nullable=True)