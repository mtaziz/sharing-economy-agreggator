#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem

class JestockeSpider(scrapy.Spider):
	name = "jestocke"
	category = "storing"
	subcategory = "space"
	allowed_domains = ["http://www.jestocke.fr"]
	# scrap boaterfly by pages
	start_urls = list(map(lambda x: "https://www.jestocke.com/location/recherche/"+str(x), range(51)))


	def parse(self, response):
		for sel in response.xpath('//article'):
			item = AdItem()
		 	empty = "unknown"
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath('div[2]/h2/a/text()').extract()[0]  
			except:
				item['title'] = empty
			try:
				item['media'] = sel.xpath('div[1]/a/@href').extract()[0]
			except:
				item['media'] = empty
			try:
				item['url'] = sel.xpath('div[2]/h2/a/@href').extract()[0]
			except:
				item['url'] = empty
			try:
				item['description'] = sel.xpath('div[2]/p/text()').extract()[0]
			except:
				item['description'] = empty
			try:
				item['location']  = sel.xpath('div[2]/p[2]/text()').extract()[0]
			except:
				item['location'] = empty
			try:
				item['latitude']  = sel.xpath('div[2]/p[3]/a/span[@class="latitude"]/text()').extract()[0]
			except:
				item['latitude'] = empty
			try:
				item['longitude'] = sel.xpath('div[2]/p[3]/a/span[@class="longitude"]/text()').extract()[0]
			except:
				item['longitude'] = empty
			try:
				item['price'] = sel.xpath('div[3]/div/div/span[@class="price-figure"]/text()').extract()[0].strip('€')
			except:
				item['price'] = empty

			try:	
				item['period'] = sel.xpath('div[3]/div/div/text()').extract()[0]
			except:
				item['period'] = empty 
			yield item
