#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import France

class CookeningSpider(scrapy.Spider):
	name = "cookening"
	category = "eating"
	subcategory = "meals"
	allowed_domains = ["https://www.cookening.com"]
	# scrap by cities
	France = France()
	cities = France.cities
	start_urls = list(map(lambda x: "https://www.cookening.com/fr/explore/"+str(x), cities))

	def parse(self, response):
		for sel in response.xpath("//ul[@id='MealCards']/li"):
			item = AdItem()
			empty = ''
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath("a/div[@id='myCarouselGroup']/div[@class='Title myCarousel']/div[@class='Info']/h3/text()").extract()[0]
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
			item['postal_code'] = 0
			
			item['latitude'] = empty
			item['longitude'] = empty

			try:
				item['price'] = sel.xpath("a/div[2]/div[2]/div/span[@class='Contribution']/strong/text()").extract()[0].strip('\n').encode('utf-8').strip('€')
				item['currency'] = "€"
			except:
				item['price'] = empty
				item['currency'] = empty

			try:
				item['period'] = sel.xpath("a/div[2]/div[2]/div/span[@class='Contribution']/span/text()").extract()[0]
			except:
				item['period'] = empty
			
			yield item
