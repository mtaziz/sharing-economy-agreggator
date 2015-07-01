#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.geoloc import geocode
from robot.country import France, Spain, all_cities

class AirbnbSpider(scrapy.Spider):
	name = "airbnb"
	category = "housing"
	#subcategory = "room"
	allowed_domains = ["https://www.airbnb.com"]
	# scrap by cities
	France = France()
	cities = France.cities
	
	cities_fr = all_cities()
	start_urls_0 = list(map(lambda x: "https://www.airbnb.fr/s/"+str(x), cities_fr))
	
	apartment_found = "room_types[]=Entire+home%2Fapt"
	start_apt = [url+"?"+apartment_found+"&page="+str(x) for url in start_urls_0 for x in range(10)]
	
	room_found = "room_types[]=Private+room&room_types[]=Shared+room"
	start_room = [url+"?"+room_found+"&page="+str(x) for url in start_urls_0 for x in range(10)]
	start_urls = start_apt + start_room

	def parse(self, response):
		for sel in response.xpath('//div[@data-id]'):
			item = AdItem()
			empty = ''
			item['source'] = self.name
			item['category'] = self.category
			if "Private+room" in response.url:
				item['subcategory'] = "room"
			elif "home" in response.url:
				item['subcategory']	= "apartment"
			else:
				raise("unable to detect home/room filter")
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
 			try:
 				item['location'] = geocode(item['latitude'], item['longitude'])
			except:
				item['location'] = empty
			try:
				item['price'] = sel.xpath('div/a[2]/div/span/text()').extract()[0]
				item['currency'] = "€"
			except:
				item['price'] = empty
				item['currency'] = empty
			
			item['period'] = empty
			
			yield item
