#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime

class SejourningSpider(scrapy.Spider):
	name = "sejourning"
	category = "housing"
	subcategory = "apartment"
	allowed_domains = ["https://www.sejourning.com"]
	# scrap by cities
	cities = [
		"Paris","Amiens","Nancy",
		"Rouen","Caen","Evreux","Saint Lo","Rennes","Quimper","Morlaix","Vannes","Strasbourg","Nantes","Clermont Ferrand","Bordeaux","Dax","Chambery",
		"Poitiers","Perpignan","Nimes","Montpellier","Marseille","Nice","Lyon","Toulouse","Limoges","Besancon","Troyes","Orléans","Le mans","Gap","Millau",
		"Brives","Reims","Avallon","Le Puy en Velay","Aurillac","Privas","Valence","Agen","Saint Brieuc","Cherbourg","Charleville","Nevers","Angers","Pau"
	]

	start_urls_0 = list(map(lambda x: "https://www.sejourning.com/fr/location/"+str(x), cities))
	start_urls = [url+"/"+cities[start_urls_0.index(url)]+"-"+str(x)+".html" for url in start_urls_0 for x in range(10)]

	def parse(self, response):
		for sel in response.xpath("//div[@class='sej-resultAlign']"):
			item = AdItem()
			empty = 'unknown'
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath("div/div[2]/div/h2/a/text()").extract()[0]
			except: 
				item['title'] = empty

			item['media'] = empty

			try:
				item['url'] = self.allowed_domains[0] + sel.xpath('div/div/a/@href').extract()[0]
			except:
				item['url'] = empty
			
			try:		
				item['description'] = sel.xpath("div/div[2]/div/h2[2]/text()").extract()[0]
			except:
				item['description'] = empty

			try:
				item['location'] = sel.xpath("div/div[2]/div[@class='offer__details']/div[@class='offer__subtitle']/text()").extract()[0]
			except:
				item['location'] = empty

			
			item['latitude'] = empty
			item['longitude'] = empty

			try:
				item['price'] = sel.xpath("div/div[2]/div[3]/h2/text()").extract()[0].strip('\n').encode('utf-8').strip('€')
			except:
				item['price'] = empty

			try:
				item['period'] = sel.xpath("div/div[2]/div[3]/h2[2]/text()").extract()[0]
			except:
				item['period'] = empty
			
			yield item
