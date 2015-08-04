#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import France
import urllib
import re

pattern = re.compile('\d{1,}')

class AirbnbSpider(scrapy.Spider):
	name = "airbnb"
	category = "housing"
	#subcategory = "room"
	allowed_domains = ["https://www.airbnb.com"]
	# scrap by cities
	France = France()
	cities = France.cities
	start_urls_0 = list(map(lambda x: "https://www.airbnb.fr/s/"+str(x), cities))
	start_urls = [url+"?page="+str(x) for url in start_urls_0 for x in range(10)]
	
	
	def parse(self, response):
		for sel in response.xpath('//div[@data-id]'):
			item = AdItem()
			empty = ''
			item['source'] = self.name
			item['category'] = self.category
			
			try:
				item['title'] = sel.xpath('@data-name').extract()[0]
			except: 
				item['title'] = empty

			try:	
				item['media'] = sel.xpath('div/a/div/img/@src').extract()[0]
			except: 
				item['media'] = empty

			try:
				item['url'] = self.allowed_domains[0] + sel.xpath('@data-url').extract()[0].split('?')[0]
			except:
				item['url'] = empty

			try:		
				item['description'] = sel.xpath('div[2]/div/div[@itemprop="description"]/a/text()').extract()[0]

			except:
			
				item['description'] = sel.xpath('@data-name').extract()[0]
			
			if "Chambre" in item['description']:
				item['subcategory'] = "room"
			else:
				item['subcategory']	= "apartment"
			
			try:
				item['evaluations'] = 0
				find = re.search(pattern, item['description'])
				if find:
					item['evaluations'] = int(find.group())
			except:
				item['evaluations'] = 0
			
			item['latitude'] = sel.xpath('@data-lat').extract()[0]
			item['longitude'] = sel.xpath('@data-lng').extract()[0]
 			try:
 				item['location'] = urllib.unquote(response.url.split('?')[0].split('s/')[-1])
			except:
				item['location']= empty
		        item['postal_code'] = 0		
			try:
				item['price'] = sel.xpath('div/a[2]/div/span/text()').extract()[0]
				item['currency'] = "€"
			except:
				item['price'] = empty
				item['currency'] = empty
			
			item['period'] = "nuit"
			
			yield item
