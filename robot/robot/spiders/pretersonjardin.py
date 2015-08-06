#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import France

class HousetripSpider(scrapy.Spider):
	name = "pretersonjardin"
	category = "eating"
	subcategory = "gardens"
	allowed_domains = ["http://www.pretersonjardin.com"]
	pages = 18*range(1,1000)
	start_urls = list(map(lambda x: "http://www.pretersonjardin.com/annonces/toutes-les-annonces/Page-%s.html"%str(x), range(1,100)))
	France = France()
	geo = France.geo

	def parse(self, response):
		for sel in response.xpath('//tr'):
			item = AdItem()
			empty = ''
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath('td[@id="colonne4"]/div[@id="title_ad"]/a/text()').extract()[0].strip(' ').title()
			except: 
				item['title'] = empty

			item['media'] = empty

			try:
				item['url'] = sel.xpath('td[@id="colonne4"]/div[@id="title_ad"]/a/@href').extract()[0]
			except:
				item['url'] = empty
			
			try:		
				item['description'] = sel.xpath('td[@id="colonne4"]/div[@id="text_ad"]/a/text()').extract()[0]
			except:
				item['description'] = empty

			try:
				item['location'] = sel.xpath('td[@id="colonne3"]/text()').extract()[0].strip(' ').title()
			except:
				item['location'] = empty

			try:
				item['latitude'] = self.geo[item['location']]['lat']
			except:
				item['latitude'] = empty
			try:
				item['longitude'] = self.geo[item['location']]['lon']
			except:
				item['longitude'] = empty
			item['price'] = empty
			item['currency'] = empty
			
			try:
				item['period'] = sel.xpath('td[@id="colonne5"]/div/text()').extract()[0]
			except:
				item['period'] = empty
			item['postal_code'] = empty
			item['evaluations'] = empty			
			yield item
