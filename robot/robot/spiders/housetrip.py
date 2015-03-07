#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from geopy.geocoders import Nominatim 

class HousetripSpider(scrapy.Spider):
	name = "housetrip"
	category = "housing"
	subcategory = "apartment"
	allowed_domains = ["http://www.housetrip.fr"]
	# scrap by cities
	cities = [
		"Paris","Amiens","Nancy",
		"Rouen","Caen","Evreux","Saint Lo","Rennes","Quimper","Morlaix","Vannes","Strasbourg","Nantes","Clermont Ferrand","Bordeaux","Dax","Chambery",
		"Poitiers","Perpignan","Nimes","Montpellier","Marseille","Nice","Lyon","Toulouse","Limoges","Besancon","Troyes","Orléans","Le mans","Gap","Millau","Brives"
	]
	#cities = ['paris', 'nantes', 'lille', 'bordeaux', 'nancy', 'nice']
	start_urls_0 = list(map(lambda x: "http://www.housetrip.fr/fr/rechercher/"+str(x), cities))
	start_urls = [url+"?page="+str(x) for url in start_urls_0 for x in range(100)]
	

	def parse(self, response):
		for sel in response.xpath('//div[@data-element-id]'):
			item = AdItem()
			empty = 'unknown'
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath('div[2]/h3/a/text()').extract()[0]
			except: 
				item['title'] = empty

			try:	
				item['media'] = sel.xpath('div[1]/@style').extract()[0].split('(')[1].split(')')[0]
			except: 
				item['media'] = empty

			try:
				item['url'] = sel.xpath('div[2]/h3/a/@href').extract()[0]
			except:
				item['url'] = empty
			
			try:		
				desc0 = sel.xpath('div[2]/div/ul[1]/li[1]/text()').extract()[0]
				desc1 = sel.xpath('div[2]/div/ul[1]/li[2]/text()').extract()[0]
				desc2 = sel.xpath('div[2]/div/ul[2]/li/text()').extract()[0]
				item['description'] = desc0 + " " + desc1 + " " + desc2
			except:
				item['description'] = empty

			try:
				item['location'] = sel.xpath('div[2]/h4/text()').extract()[0]
			except:
				item['location'] = empty

			
			item['latitude'] = empty
			item['longitude'] = empty

			try:
				item['price'] = sel.xpath('div[3]/div/p/text()').extract()[0].strip('€')
			except:
				item['price'] = empty

			try:
				item['period'] = sel.xpath('div[3]/div/p[2]/text()').extract()[0]
			except:
				item['period'] = empty
			
			yield item
