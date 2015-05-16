#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
from robot.country import France

class JestockeSpider(scrapy.Spider):
	name = "jestocke"
	category = "storing"
	subcategory = "space"
	allowed_domains = ["http://www.jestocke.fr"]
	France = France()
	cities = France.cities
	start_urls_0 = list(map(lambda x: "https://www.jestocke.com/s/"+str(x), cities))
	start_urls = [url+"?"+"page="+str(x) for url in start_urls_0 for x in range(10)]

	def parse(self, response):
		for sel in response.xpath('//article[@id]'):
			item = AdItem()
		 	empty = ""
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath('a/div[3]/div/h3/text()').extract()[0].strip(' \n')
			except:
				item['title'] = empty
			try:
				item['media'] = self.allowed_domains[0] + sel.xpath('a/div/img/@src').extract()[0]
			except:
				item['media'] = empty
			try:
				item['url'] = self.allowed_domains[0] + sel.xpath('a/@href').extract()[0]
			except:
				item['url'] = empty
			try:
				item['description'] = sel.xpath('a/div[3]/p/strong/text()').extract()[0]
			except:
				item['description'] = empty
			try:
				item['location']  = sel.xpath('a/div[3]/div/h3/text()[3]').extract()[0]
			except:
				item['location'] = empty
			
			item['latitude'] = empty
			item['longitude'] = empty
			
			try:
				item['price'] = sel.xpath('a/div[@class="ad-item_price"]/div/div/text()').extract()[0].encode('utf-8').split('€')[0]
				item['currency'] = "€"
			except:
				item['price'] = empty
				item['currency'] = empty

			try:	
				item['period'] = sel.xpath('a/div[@class="ad-item_price"]/div/div[2]/text()').extract()[0]
			except:
				item['period'] = empty 
			yield item
