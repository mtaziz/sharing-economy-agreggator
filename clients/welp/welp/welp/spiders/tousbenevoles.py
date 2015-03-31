# -*- coding: utf-8 -*-
import scrapy
from welp.items import WelpItem

class ExampleSpider(scrapy.Spider):
    name = "tousbenevoles"
    allowed_domains = ["http://www.tousbenevoles.org"]
    start_urls = list(map(lambda x: "http://www.tousbenevoles.org/trouver-une-mission-benevole?page=%s" %str(x), range(1,100)))

    def parse(self, response):

        for sel in response.xpath('//div[@id="resultats"]/div[@class="col-xs-12 apercu"]'):
			item = WelpItem()
			empty = 'unknown'
			item['source'] = self.name
			try:

				item['category'] = sel.xpath("div[3]/ul/li/text()").extract()[0] + "/" + sel.xpath("div[3]/ul/li[2]/text()").extract()[0]
			except:
				item['category'] = empty
			try:
				item['title'] = sel.xpath('a/@title').extract()[0]
			except: 
				item['title'] = empty

			try:	
				item['media'] = sel.xpath('img/@src').extract()[0]
			except: 
				item['media'] = empty
			
			try:		
				item['description'] = sel.xpath('div/text()').extract()[0]
			except:
				item['description'] = empty

			try:
				item['address'] = sel.xpath('div[2]/ul/li/text()').extract()[0]
			except:
				item['address'] = empty
			item['latitude'] = empty
			item['longitude'] = empty

			try:
				item['ong_name'] = sel.xpath('strong/text()').extract()[0]
			except:
				item['ong_name'] = empty
			try:
				item['availability'] = sel.xpath('div[2]/ul/li[2]/text()').extract()[0]
			except: 
				item['availability'] = empty

			yield item
