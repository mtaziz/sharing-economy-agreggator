#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from geopy.geocoders import Nominatim 

class HousetripSpider(scrapy.Spider):
	name = "chambrealouer"
	category = "housing"
	subcategory = "room"
	allowed_domains = ["http://fr.chambrealouer.com"]
	# scrap by cities
	cities = [
		"Paris","Amiens","Nancy",
		"Rouen","Caen","Evreux","Saint Lo","Rennes","Quimper","Morlaix","Vannes","Strasbourg","Nantes","Clermont Ferrand","Bordeaux","Dax","Chambery",
		"Poitiers","Perpignan","Nimes","Montpellier","Marseille","Nice","Lyon","Toulouse","Limoges","Besancon","Troyes","Orléans","Le mans","Gap","Millau","Brives"
	]
	#cities = ['paris', 'nantes', 'lille', 'bordeaux', 'nancy', 'nice']
	start_urls = list(map(lambda x: "http://fr.chambrealouer.com/location/FR-France/"+str(x), cities))

	def parse(self, response):
		for sel in response.xpath('//div[@class="rentResult ad-list-item"]'):
			item = AdItem()
			empty = 'unknown'
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath('div[@class="detail"]/img/@alt').extract()[0]
			except: 
				item['title'] = empty

			try:	
				item['media'] = sel.xpath('div[@class="detail"]/img/@src').extract()[0]
			except: 
				item['media'] = empty

			try:
				item['url'] = sel.xpath('div[@class="detail"]/meta/@content').extract()[0]
			except:
				item['url'] = empty
			
			try:		
				item['description'] = sel.xpath('div[@class="detail"]/div/p/span/text()').extract()[0]
			except:
				item['description'] = empty

			try:
				item['location'] = sel.xpath('//div[@class="rentResult ad-list-item"]/div[@class="detail"]/div/div[@itemprop="address"]/span[@class="location"]/span/text()').extract()[0]
			except:
				item['location'] = empty

			
			item['latitude'] = sel.xpath('div[@class="detail"]/div/div[@itemprop="geo"]/meta[@itemprop="latitude"]/@content').extract()[0]
			item['longitude'] = sel.xpath('div[@class="detail"]/div/div[@itemprop="geo"]/meta[@itemprop="longitude"]/@content').extract()[0]

			try:
				price0 = sel.xpath('table/tr[2]/td[1]/text()').extract()[0].encode('utf-8').strip('€')
				price1 = sel.xpath('table/tr[2]/td[2]/text()').extract()[0].encode('utf-8').strip('€')
				price2 = sel.xpath('table/tr[2]/td[3]/text()').extract()[0].encode('utf-8').strip('€')
				item['price'] = price0 + ", " + price1 + ", " + price2 

			except:
				item['price'] = empty

			try:
				period0 = sel.xpath('table/tr/td[1]/text()').extract()[0]
				period1 = sel.xpath('table/tr/td[2]/text()').extract()[0]
				period2 = sel.xpath('table/tr/td[3]/text()').extract()[0]
				item['period'] = period0 + ", " + period1 + ", " + period2 
			except:
				item['period'] = empty
			
			yield item
