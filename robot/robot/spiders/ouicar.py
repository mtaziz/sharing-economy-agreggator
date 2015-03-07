#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from geopy.geocoders import Nominatim 

class OuicarSpider(scrapy.Spider):
	name = 'ouicar'
	category = 'moving'
	subcategory = "car"
	allowed_domains = ["http://www.ouicar.fr"]
	
	cities  = [
	"Paris","Amiens","Nancy",
	"Rouen","Caen","Evreux","Saint Lo","Rennes","Quimper","Morlaix","Vannes","Strasbourg","Nantes","Clermont Ferrand","Bordeaux","Dax","Chambery",
	"Poitiers","Perpignan","Nimes","Montpellier","Marseille","Nice","Lyon","Toulouse","Limoges","Besancon","Troyes","Orléans","Le mans","Gap","Millau","Brives"
	]

	start_urls_0 = list(map(lambda x: "http://www.ouicar.fr/car/search?where="+str(x), cities))
	start_urls = [url+"&page="+str(x) for url in start_urls_0 for x in range(100)]
	

	def parse(self, response):
		for sel in response.xpath('//tr[@data-dpt]'):
			item = AdItem()
			empty = 'unknown'
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath('td/div/a/h3/text()').extract()[0] + sel.xpath('td/div/a/h3/small/text()').extract()[0]
			except: 
				item['title'] = empty

			try:	
				item['media'] = sel.xpath('td/span/img/@src').extract()[0]
			except: 
				item['media'] = empty

			try:
				item['url'] = sel.xpath('td/div/a/@href').extract()[0]
			except:
				item['url'] = empty
			
			try:		
				desc0 = sel.xpath('td/div/p/text()').extract()[0]
				desc1 = sel.xpath('td/div/p[2]/div/text()').extract()[0]
				item['description'] = desc0 + "\n" + desc1
			except:
				item['description'] = empty

			try:
				item['location'] = sel.xpath('@data-city').extract()[0]
			except:
				item['location'] = empty

			item['latitude'] = sel.xpath('@data-lat').extract()[0]
			item['longitude'] = sel.xpath('@data-lng').extract()[0]

			try:
				item['price'] = sel.xpath('td[2]/p/text()').extract()[0].strip('€')
			except:
				item['price'] = empty

			item['period'] = empty
		
			yield item
