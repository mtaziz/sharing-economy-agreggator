#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from geopy.geocoders import Nominatim 

class HousetripSpider(scrapy.Spider):
	name = "cookening"
	category = "eating"
	subcategory = "meals"
	allowed_domains = ["https://www.cookening.com"]
	# scrap by cities
	cities = [
		"Paris","Amiens","Nancy",
		"Rouen","Caen","Evreux","Saint Lo","Rennes","Quimper","Morlaix","Vannes","Strasbourg","Nantes","Clermont Ferrand","Bordeaux","Dax","Chambery",
		"Poitiers","Perpignan","Nimes","Montpellier","Marseille","Nice","Lyon","Toulouse","Limoges","Besancon","Troyes","Orléans","Le mans","Gap","Millau",
		"Brives","Reims","Avallon","Le Puy en Velay","Aurillac","Privas","Valence","Agen","Saint Brieuc","Cherbourg","Charleville","Nevers","Angers","Pau"]
	#cities = ['paris', 'nantes', 'lille', 'bordeaux', 'nancy', 'nice']
	start_urls = list(map(lambda x: "https://www.cookening.com/fr/explore/"+str(x), cities))

	def parse(self, response):
		for sel in response.xpath("//ul[@id='MealCards']/li"):
			item = AdItem()
			empty = 'unknown'
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath('div[2]/div[2]/div/h3/text()').extract()[0]
			except: 
				item['title'] = empty

			try:	
				item['media'] = sel.xpath('a/div/img/@src').extract()[0]
			except: 
				item['media'] = empty

			try:
				item['url'] = self.allowed_domains[0] + sel.xpath('a/@href').extract()[0]
			except:
				item['url'] = empty
			
			try:		
				desc0 = sel.xpath("a/div[@class='Host']/span[@class='Name']/text()").extract()[0]
				desc1 = sel.xpath("a/div[@class='Host']/span[@class='Bio']/text()").extract()[0]
				item['description'] = desc0 + " " + desc1
			except:
				item['description'] = empty

			try:
				item['location'] = sel.xpath("a/div[2]/div[2]/div/span[@class='Place']/text()").extract()[0]
			except:
				item['location'] = empty

			
			item['latitude'] = empty
			item['longitude'] = empty

			try:
				item['price'] = sel.xpath("a/div[2]/div[2]/div/span[@class='Contribution']/strong/text()").extract()[0].strip('\n').encode('utf-8').strip('€')
			except:
				item['price'] = empty

			try:
				item['period'] = sel.xpath("a/div[2]/div[2]/div/span[@class='Contribution']/span/text()").extract()[0]
			except:
				item['period'] = empty
			
			yield item
