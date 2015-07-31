#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import France, Spain

class HousetripSpider(scrapy.Spider):
	name = "housetrip"
	category = "housing"
	subcategory = "apartment"
	allowed_domains = ["http://www.housetrip.fr"]
	France = France()
	Spain = Spain()
	cities = France.cities + Spain.cities
	start_urls_0 = list(map(lambda x: "http://www.housetrip.fr/fr/chercher-appartements-vacances/"+str(x), cities))
	start_urls = [url+"?page="+str(x) for url in start_urls_0 for x in range(100)]
	

	def parse(self, response):
		for sel in response.xpath('//li[@data-element-id]'):
			item = AdItem()
			empty = ''
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath('div[2]/h3/a/text()').extract()[0]
			except: 
				item['title'] = empty

			try:	
				item['media'] = sel.xpath('div[1]/@style').extract()[0].split('(')[1].split(')')[0].strip("'")
			except: 
				item['media'] = empty

			try:
				item['url'] = self.allowed_domains[0] + sel.xpath('div[2]/h3/a/@href').extract()[0]
			except:
				item['url'] = empty
			
			try:		
				desc0 = sel.xpath('div[2]/div/ul[1]/li[1]/text()').extract()[0]
				desc1 = sel.xpath('div[2]/div/ul[1]/li[2]/text()').extract()[0]
				#desc2 = sel.xpath('div[2]/div/ul[2]/li/text()').extract()[0]
				item['description'] = desc0 + " " + desc1 + " " 
			except:
				item['description'] = empty

			try:
				item['location'] = sel.xpath('div[2]/h4/text()').extract()[0]
			except:
				item['location'] = empty

			item['postal_code'] = '0'			
			item['evaluations'] = empty
			item['latitude'] = empty
			item['longitude'] = empty

			try:
				item['price'] = sel.xpath('div[3]/div/p/text()').extract()[0].strip('\n').encode('utf-8').strip('€')
				item['currency'] = "€"
			except:
				item['price'] = empty
				item['currency'] = empty

			try:
				item['period'] = sel.xpath('div[3]/div/p[2]/text()').extract()[0]
			except:
				item['period'] = empty
			
			yield item
