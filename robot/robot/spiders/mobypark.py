#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
from robot.country import France
import json

class MobyparkSpider(scrapy.Spider):
	name = "mobypark"
	category = "storing"
	subcategory = "space"
	allowed_domains = ["http://www.mobypark.fr"]
	France = France()
	cities = France.cities
	start_urls = list(map(lambda x: "https://www.mobypark.fr/api/offers?format=json?distance=15&radius=15&q="+str(x), cities))
	
	def parse(self, response):
		jsonresponse = json.loads(response.body_as_unicode())
		result = jsonresponse["result"]
		if result.has_key('offers'):
			results=result["offers"]

			for sel in results:
				item = AdItem()
			 	empty = ""
				item['source'] = self.name
				item['category'] = self.category
				item['subcategory'] = self.subcategory
				
				try:
					item['title'] = sel['car_park']['location']['formatted_address']
				except:
					item['title'] = empty
				try:
					item['media'] = sel["car_park"]["first_picture"]["url"]
					print item['media']
				except:
					item['media'] = empty
				try:
					url_id = sel["car_park"]["id"]
					item['url'] = self.allowed_domains[0]+"/carpark/"+str(url_id)+"/show"
				except:
					item['url'] = empty
				try:
					item['description'] = sel["car_park"]["description"]
				except:
					item['description'] = empty
				try:
					item['location']  = sel['car_park']['location']['formatted_address']
				except:
					item['location'] = empty
				
				try:
					item['latitude'] = sel['car_park']['location']['latitude']
				except:
					item['latitude'] = empty
				
				try:
					item['longitude'] = sel['car_park']['location']['longitude']
				except:
					item['longitude'] = empty
				
				try:
					item['price'] = sel["car_park"]["day_rate"]
					item['currency'] = "€"
				except:
					item['price'] = empty
					item['currency'] = empty
				
				try:
					item['period'] = sel["car_park"]["minimal_duration"]
				except:
					item['period'] = empty
					
				yield item
			