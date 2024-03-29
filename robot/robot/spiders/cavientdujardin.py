#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import France

class HousetripSpider(scrapy.Spider):
	name = "cavientdujardin"
	category = "eating"
	subcategory = "vegetables"
	allowed_domains = ["http://www.cavientdujardin.com"]
	start_urls = list(map(lambda x: "http://www.cavientdujardin.com/petites-annonces/0-0-0-0-%s.html"%str(x), range(1,10)))
	France = France()
	geo = France.geo
	def parse(self, response):
		for sel in response.xpath('//div[@class="LigneAnnonce"]'):
			item = AdItem()
			empty = ''
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath('div[@class="ListDet"]/a[@class="ListTitre1"]/text()').extract()[0]
			except: 
				item['title'] = empty
			try:
				item['media'] = sel.xpath('div[@class="ListImg"]/img/@src').extract()[0]
			except:
				item['media'] = empty
			try:
				item['url'] = self.allowed_domains[0] + sel.xpath('div[@class="ListDet"]/a/@href').extract()[0]
			except:
				item['url'] = empty
			
			try:		
				item['description'] = sel.xpath('div[@class="ListDet"]/a[@class="ListTitre"]/text()').extract()[0]
			except:
				item['description'] = empty

			try:
				item['location'] = sel.xpath('div[@class="ListDet"]/span[@class="ville"]/text()').extract()[0]
			except:
				item['location'] = empty
			item['postal_code'] = empty
			try:
				item['latitude'] = float(self.geo[item['location']]['lat'])
			except:
				item['latitude'] = empty
			try:
				item['longitude'] = float(self.geo[item['location']]['lon'])
			except:
				item['longitude'] = empty

			try:
				item['price'] = sel.xpath('div[@class="ListDet"]/span[@class="ListPrix"]/text()').extract()[0]
				item['currency'] = "€"
			except:
				item['price'] = empty
				item['currency'] = empty

			try:
				item['period'] = sel.xpath('div[@class="ListCol1"]/text()').extract()[0]
			except:
				item['period'] = empty
			item['evaluations'] = empty
			yield item
