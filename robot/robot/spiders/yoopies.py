#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.geoloc import geocode
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
		for sel in response.xpath('//div[@data-id]'):
			item = AdItem()
			empty = ''
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory
			try:
				item['title'] = sel.xpath('@data-name').extract()[0]
			except: 
				item['title'] = empty

			try:	
				item['media'] = sel.xpath('div/a/div/img/@src').extract()[0]
			except: 
				item['media'] = empty

			try:
				item['url'] = self.allowed_domains[0] + sel.xpath('@data-url').extract()[0]
			except:
				item['url'] = empty
			
			try:		
				item['description'] = sel.xpath('div[2]/div/a[2]/div/text()').extract()[0].strip(' \n')

			except:
				item['description'] = empty

			
			item['latitude'] = sel.xpath('@data-lat').extract()[0]
			item['longitude'] = sel.xpath('@data-lng').extract()[0]
 			item['location'] = geocode(item['latitude'], item['longitude'])
			try:
				item['price'] = sel.xpath('div/a[2]/div/span/text()').extract()[0]
			except:
				item['price'] = empty

			item['period'] = empty
			
			yield item
