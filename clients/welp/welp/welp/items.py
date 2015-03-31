# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WelpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	source = scrapy.Field()
	title = scrapy.Field()    
	volunteer_name = scrapy.Field()
	ong_name = scrapy.Field()
	address = scrapy.Field()
	latitude = scrapy.Field()
	longitude = scrapy.Field()
	category = scrapy.Field()
	availability = scrapy.Field()
	description = scrapy.Field()
	media = scrapy.Field()
