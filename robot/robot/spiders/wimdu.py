#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime

class WimduSpider(scrapy.Spider):
	name = "wimdu"
	category = "housing"
	subcategory = "apartment"
	allowed_domains = ["http://www.wimdu.fr"]
	# scrap by cities
	cities = [
		"Paris","Amiens","Nancy",
		"Rouen","Caen","Evreux","Saint Lo","Rennes","Quimper","Morlaix","Vannes","Strasbourg","Nantes","Clermont Ferrand","Bordeaux","Dax","Chambery",
		"Poitiers","Perpignan","Nimes","Montpellier","Marseille","Nice","Lyon","Toulouse","Limoges","Besancon","Troyes","Orléans","Le mans","Gap","Millau",
		"Brives","Reims","Avallon","Le Puy en Velay","Aurillac","Privas","Valence","Agen","Saint Brieuc","Cherbourg","Charleville","Nevers","Angers","Pau"]
	#cities = ['paris', 'nantes', 'lille', 'bordeaux', 'nancy', 'nice']
	start_urls_0 = list(map(lambda x: "http://www.wimdu.fr/"+str(x), cities))
	start_urls = [url+"?page="+str(x) for url in start_urls_0 for x in range(10)]
	

	def parse(self, response):
		for sel in response.xpath("//ul[@id='results']/li"):
			item = AdItem()
			empty = 'unknown'
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath("div/div[2]/div[@class='offer__details']/h3/a/text()").extract()[0]
			except: 
				item['title'] = empty

			try:	
				item['media'] = sel.xpath('div/div/a/img[2]/@data-src').extract()[0]
			except: 
				item['media'] = empty

			try:
				item['url'] = self.allowed_domains[0] + sel.xpath('div/div/a/@href').extract()[0]
			except:
				item['url'] = empty
			
			try:		
				item['description'] = sel.xpath("div/div[2]/div[@class='offer__details']/div[@class='offer__description']/text()").extract()[0]
			except:
				item['description'] = empty

			try:
				item['location'] = sel.xpath("div/div[2]/div[@class='offer__details']/div[@class='offer__subtitle']/text()").extract()[0]
			except:
				item['location'] = empty

			
			item['latitude'] = empty
			item['longitude'] = empty

			try:
				item['price'] = sel.xpath("div/div[2]/div[@class='price price--mini js-price-per-night']/div/text()[2]").extract()[0].strip('\n').encode('utf-8').strip('€')
			except:
				item['price'] = empty

			try:
				item['period'] = sel.xpath('div/div[2]/div[@class='price price--mini js-price-per-night']/div[2]/text()').extract()[0]
			except:
				item['period'] = empty
			
			yield item
