#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime

class HousetripSpider(scrapy.Spider):
	name = "monsieurparking"
	category = "storing"
	subcategory = "parking"
	allowed_domains = ["http://www.monsieurparking.com"]
	# scrap by cities
	cities = [
		"Paris","Amiens","Nancy",
		"Rouen","Caen","Evreux","Saint Lo","Rennes","Quimper","Morlaix","Vannes","Strasbourg","Nantes","Clermont Ferrand","Bordeaux","Dax","Chambery",
		"Poitiers","Perpignan","Nimes","Montpellier","Marseille","Nice","Lyon","Toulouse","Limoges","Besancon","Troyes","Orléans","Le mans","Gap","Millau","Brives"
	]
	#cities = ['paris', 'nantes', 'lille', 'bordeaux', 'nancy', 'nice']
	start_urls = list(map(lambda x: "http://www.monsieurparking.com/location/"+str(x)+".html", cities))

	def parse(self, response):
		for sel in response.xpath("//div[@id='loginbox']"):
			item = AdItem()
			empty = 'unknown'
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath('div/div/div/div/p/a/text()').extract()[0]
			except: 
				item['title'] = empty

			try:	
				item['media'] = sel.xpath('div[@class="detail"]/img/@src').extract()[0]
			except: 
				item['media'] = empty

			try:
				item['url'] = sel.xpath("div/div/div/div/p/a/@href").extract()[0]
			except:
				item['url'] = empty
			
			try:		
				desc0 = sel.xpath('div/div/div/div/span/text()').extract()[0]
				desc1 = sel.xpath('div/div/div/div/span[2]/text()').extract()[0]
				item['description'] = desc0 + ", " + desc1
			except:
				item['description'] = empty

			try:
				item['location'] = response.xpath("div/div/div/div/p/a/text()").extract()[0].split(' ')[-1]

			except:
				item['location'] = empty

			
			item['latitude'] = empty
			item['longitude'] = empty

			try:
				item['price'] = sel.xpath("div/div/div/div/span[3]/text()").extract()[0].split('/')[0].encode('utf-8').strip('€')

			except:
				item['price'] = empty

			try:
				item['period'] = item['price'] = sel.xpath("div/div/div/div/span[3]/text()").extract()[0].split('/')[1] 
			except:
				item['period'] = empty
			
			yield item
