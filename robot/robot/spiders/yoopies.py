#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
#from robot.geoloc import geocode
from robot.country import France

class yoopiesSpider(scrapy.Spider):
	name = "yoopies"
	category = "daily"
	subcategory = "babysitting"
	allowed_domains = ["https://yoopies.fr"]
	# scrap by cities
	France = France()
	cities = France.cities

	start_urls = list(map(lambda x: "https://yoopies.fr/recherche-baby-sitting/results?c="+str(x), cities))

	def parse(self, response):
		for sel in response.xpath('//article'):
			item = AdItem()
			empty = ''
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory
			try:
				item['title'] = sel.xpath('a/div[2]/header/h1/text()').extract()[0]
			except: 
				item['title'] = empty

			try:	
				item['media'] = sel.xpath('a/aside/figure/img/@src').extract()[0]
			except: 
				item['media'] = empty

			try:
				item['url'] = sel.xpath('a/@href').extract()[0]
			except:
				item['url'] = empty
			
			try:		
				item['description'] = sel.xpath('a/div[2]/p[@class="description"]/text()').extract()[0].strip('\n')

			except:
				item['description'] = empty

			try:
				item['latitude'] = sel.xpath('a/@data-latitude').extract()[0]
			except:
				item['latitude'] = empty
			try:
				item['longitude'] = sel.xpath('a/@data-longitude').extract()[0]
 			except:
 				item['longitude'] = empty
 			
 			try:
 				item['location'] = sel.xpath('a/aside/div[@class="user-city"]/text()').extract()[0]
			except:
				item['location'] = empty

			item['postal_code'] = empty
			item['evaluations'] = empty
			item['price'] = empty
			item['currency'] = empty
			item['period'] = empty
			
			yield item
