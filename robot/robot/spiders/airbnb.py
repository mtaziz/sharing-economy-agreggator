#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime

class AirbnbSpider(scrapy.Spider):
	name = "airbnb"
	category = "housing"
	subcategory = "apartment"
	allowed_domains = ["https://www.airbnb.com"]
	# scrap by cities
	cities = [
		"Paris","Amiens","Nancy",
		"Rouen","Caen","Evreux","Saint Lo","Rennes","Quimper","Morlaix","Vannes","Strasbourg","Nantes","Clermont Ferrand","Bordeaux","Dax","Chambery",
		"Poitiers","Perpignan","Nimes","Montpellier","Marseille","Nice","Lyon","Toulouse","Limoges","Besancon","Troyes","Orléans","Le mans","Gap","Millau",
		"Brives","Reims","Avallon","Le Puy en Velay","Aurillac","Privas","Valence","Agen","Saint Brieuc","Cherbourg","Charleville","Nevers","Angers","Pau"]
	#cities = ['paris', 'nantes', 'lille', 'bordeaux', 'nancy', 'nice']
	start_urls_0 = list(map(lambda x: "https://www.airbnb.fr/s/"+str(x), cities))
	start_urls = [url+"?page="+str(x) for url in start_urls_0 for x in range(10)]
	

	def parse(self, response):
		for sel in response.xpath('//div[@data-id]'):
			item = AdItem()
			empty = 'unknown'
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

			item['location'] = empty
			item['latitude'] = sel.xpath('@data-lat').extract()[0]
			item['longitude'] = sel.xpath('@data-lng').extract()[0]

			try:
				item['price'] = sel.xpath('@data-price').extract()[0].encode('utf-8').strip('€')
			except:
				item['price'] = empty

			item['period'] = empty
			
			yield item
