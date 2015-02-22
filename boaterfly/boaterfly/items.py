# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BoaterflyItem(scrapy.Item):
    title = scrapy.Field()
    media = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    location = scrapy.Field()
    distance = scrapy.Field()
    price = scrapy.Field()
    period = scrapy.Field()  
    owner = scrapy.Field()
