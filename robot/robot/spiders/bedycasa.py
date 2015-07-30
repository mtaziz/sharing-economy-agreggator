#-*- encoding:utf-8 -*-
import requests
import json
import scrapy 
from robot.items import AdItem
from robot.country import France

#Bedycasa API documentation: http://www.bedycasa.com/api/doc/index.html
#generate access_token: valid 3600s

url = "https://www.bedycasa.com/oauth/v2/token"
client_id = "21_48jkpjawhuec0ock0ocgkcco00ocww80c8ookw08wwo0ck0wg8"
client_secret = "40h63xgptxwk4sgsw404g04c0ogoskww4ckoo04ok440c48wg"
grant_type = "client_credentials"
params = {"client_id":client_id, "client_secret":client_secret, "grant_type":grant_type}
req_token = requests.get(url=url, params=params)
result_token = json.loads(req_token.text)
access_token = result_token["access_token"]
print access_token



class BedycasaSpider(scrapy.Spider):
	name = "bedycasa"
	category = "housing"
	subcategory = "room"
	allowed_domains = ["https://www.bedycasa.com"]
	start_urls = list(map(lambda x:"https://fr.bedycasa.com/api/rooms?api_key=%s&page=%s"%(access_token, str(x)), range(10)))

	def parse(self, response):
		jsonresponse = json.loads(response.body_as_unicode())
		#print jsonresponse
		results = jsonresponse["_embedded"]['items']
		for sel in results:
			item = AdItem()
		 	empty = ""
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory
			
			try:
				item['title'] = sel['category']['label']
			except:
				item['title'] = empty
			try:
				item['media'] = sel["defaultPicture"]
			except:
				item['media'] = empty
			try:
				item['url'] = self.allowed_domains[0] + sel['_links']['bedycasa_url']['href']
			except:
				item['url'] = empty
			try:
				item['description'] = sel['description']
			except:
				item['description'] = empty
			try:
				item['location']  = sel['_embedded']['city']
			except:
				item['location'] = empty
		    try:
				item['postal_code'] = sel['_embedded']['postalCode']
			except:	
				item['postal_code'] = empty
			try:
				item['latitude'] = sel['_embedded']['latitude']
			except:
				item['latitude'] = empty
			
			try:
				item['longitude'] = sel['_embedded']['longitude']
			except:
				item['longitude'] = empty
			
			try:
				item['price'] = sel["price"]["price"]
				item['currency'] = sel["price"]["currency"]
				item['period'] = sel["price"]["wording"]
			except:
				item['price'] = empty
				item['currency'] = empty
				item['period'] = empty
				
			yield item
		