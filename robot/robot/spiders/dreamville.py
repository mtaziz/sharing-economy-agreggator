#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
from robot.country import France
import json

class JestockeSpider(scrapy.Spider):
	name = "dreamville"
	allowed_domains = ["http://api.alterre.org"]
	start_urls = ["http://localhost:8888/api/ads?zipcode=76&token=ea2e5b417fa5df4d5891a88c6114edcc"]

	def parse(self, response):
		jsonresponse = json.loads(response.body_as_unicode())
		results = jsonresponse["ads"]
		for sel in results:
			item = AdItem()
		 	empty = ""
			item['category'] = sel['category']
			item['subcategory'] = sel['subcategory']
			
			try:
				item['title'] = sel['title']
			except:
				item['title'] = empty
			try:
				item['media'] = sel["media"]

			except:
				item['media'] = empty
			try:
				item['url'] = sel['url']

			except:
				item['url'] = empty
			try:
				item['description'] = sel['description']
			except:
				item['description'] = empty
			try:
				item['location']  = sel['location']
			except:
				item['location'] = empty
			
			try:
				item['latitude'] = sel['latitude']
			except:
				item['latitude'] = empty
			
			try:
				item['longitude'] = sel['longitude']
			except:
				item['longitude'] = empty
			
			try:
				item['price'] = sel["price"]
				item['currency'] = "EUR"
			
			except:
				item['price'] = empty
				item['currency'] = empty
			
			try:
				item['period'] = sel["period"]			
			except:
				item['period'] = empty	
				
			yield item
		
