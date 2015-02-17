# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DrivyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    media = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    location = scrapy.Field()
    distance = scrapy.Field()
    price = scrapy.Field()
    period = scrapy.Field()  
    owner = scrapy.Field()

    pass
