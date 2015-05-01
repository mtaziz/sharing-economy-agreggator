#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.geoloc import geocode

class VideDressingSpider(scrapy.Spider):
	name = "videdressing"
	category = "daily"
	subcategory = "dressing"
	allowed_domains = ["http://www.videdressing.com"]
	
	start_urls = list(map(lambda x: "http://www.videdressing.com/femme/c-c5988.html#uc/c-c5988-pg%s.json"% str(x), range(1, 1000)))
	
	def parse(self, response):
		for sel in response.xpath('//li[@data-id_product]'):
			item = AdItem()
			empty = ''
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.category
			
			try:
				item['title'] = sel.xpath('a/p/strong/text()').extract()[0]
			except: 
				item['title'] = empty

			try:	
				item['media'] = sel.xpath('a/figure/span/img/@src').extract()[0]
			except: 
				item['media'] = empty

			try:
				item['url'] = self.allowed_domains[0] + sel.xpath('a/@href').extract()[0]
			except:
				item['url'] = empty
			
			try:		
				item['description'] = sel.xpath('a/figure/span/img/@alt').extract()[0]

			except:
				item['description'] = empty

			
			item['latitude'] = empty
			item['longitude'] = empty
			item['location'] = empty
			try:
				item['price'] = sel.xpath('a/p/span[2]/span/text()').extract()[0]
			except:
				item['price'] = empty

			item['period'] = empty
			
			yield item
