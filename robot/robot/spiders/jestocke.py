#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
from robot.country import France
import json

class JestockeSpider(scrapy.Spider):
	name = "jestocke"
	category = "storing"
	subcategory = "space"
	allowed_domains = ["http://www.jestocke.fr"]
	start_urls = ["https://www.jestocke.com/api/stockage.json?api_key=c5c2a77d-92ce-4126-a265-614e8b510d93&hitsPerPage=1000"]

	def parse(self, response):
		jsonresponse = json.loads(response.body_as_unicode())
		#print jsonresponse
		results = jsonresponse["hits"]
		for sel in results:
			item = AdItem()
		 	empty = ""
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory
			
			try:
				item['title'] = sel['title']
			except:
				item['title'] = empty
			try:
				item['media'] = sel["pictures"][0]
			except:
				item['media'] = empty
			try:
				item['url'] = sel['url']
			except:
				item['url'] = empty
			try:
				item['description'] = sel['comment']
			except:
				item['description'] = empty
			try:
				item['location']  = sel['address']
			except:
				item['location'] = empty
			
			try:
				item['latitude'] = sel['lat']
			except:
				item['latitude'] = empty
			
			try:
				item['longitude'] = sel['lng']
			except:
				item['longitude'] = empty
			
			try:
				item['price'] = sel["unit_month_price_with_fee"]
				item['currency'] = "€"
				item['period'] = "par mois"
			except:
				item['price'] = empty
				item['currency'] = empty
				item['period'] = empty
				
			yield item
		