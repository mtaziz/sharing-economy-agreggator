#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import France

class SejourningSpider(scrapy.Spider):
	name = "sejourning"
	category = "housing"
	subcategory = "apartment"
	allowed_domains = ["https://www.sejourning.com"]

	start_urls = list(map(lambda x: "https://www.sejourning.com/api/f728fe567cfba806b16f96a709b0fbfed7207144/hostings.xml?country=france&limit=100&page="+str(x), xrange(1,69)))

	def parse(self, response):
		for sel in response.xpath("//hosting"):
			item = AdItem()
			empty = ''
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath("title/text()").extract()[0]
			except: 
				item['title'] = empty

			try:
				item['media'] = sel.xpath("photo/text()").extract()[0]
			except:
				item['media'] = empty
			try:
				item['url'] = sel.xpath('url/text()').extract()[0]
			except:
				item['url'] = empty
			
			try:		
				item['description'] = sel.xpath("description/text()").extract()[0][:300]+'...'
			except:
				item['description'] = empty

			try:
				item['location'] = sel.xpath("short_address/text()").extract()[0]
			except:
				item['location'] = empty

			try:
				item['postal_code'] = sel.xpath("zip/text()").extract()[0]
			except:
				item['location'] = empty

			try:
				item['latitude'] = sel.xpath("latitude/text()").extract()[0]
			except:
				item['latitude'] = empty
			try:
				item['longitude'] = sel.xpath("longitude/text()").extract()[0]
			except:
				item['longitude'] = empty
			try:
				item['price'] = sel.xpath("price_day/text()").extract()[0]
			except:
				item['price'] = empty
			try:
				item['currency'] = sel.xpath("currency/text()").extract()[0]
			except:
				item['currency'] = empty
			try:
				item['period'] = "jour"
			except:
				item['period'] = empty
			try:
				item['evaluations'] = sel.xpath("notoriety/text()").extract()[0]
			except:
				item['period'] = empty
			
			yield item
