#! -*- coding: utf-8 -*-

"""
Web Scraper Project

Scrape data from a regularly updated website jestocke.fr and
save to a database (postgres).

Database models part - defines table for storing scraped data.
Direct run will create the table....


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


def create_jestockedeals_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class JestockeDeals(DeclarativeBase):
    """Sqlalchemy deals model"""
    __tablename__ = "jestockedeals"

    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    media = Column('media', String, nullable=True)
    link = Column('link', String, nullable=True)
    desc = Column('desc', String, nullable=True)
    location = Column('location', String, nullable=True)
    latitude = Column('latitude', String, nullable=True)
    longitude = Column('longitude', String, nullable=True)
    price = Column('price', String, nullable=True)
    unit = Column('unit', String, nullable=True)
    duration = Column('duration', String, nullable=True)