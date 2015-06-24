#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import France

class VizeatSpider(scrapy.Spider):
	name = "vizeat"
	category = "eating"
	subcategory = "meals"
	allowed_domains = ["https://fr.vizeat.com"]
	# scrap by cities
	France = France()
	cities = France.cities
	start_urls = list(map(lambda x: "https://fr.vizeat.com/events/search?q="+str(x), cities))

	def parse(self, response):
		for sel in response.xpath('//div[@class="itemInside event-box p15"]'):
			item = AdItem()
			empty = ''
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath('a/img/@title').extract()[0]
			except: 
				item['title'] = empty

			try:	
				item['media'] = sel.xpath('a/img/@src').extract()[0]
			except: 
				item['media'] = empty

			try:
				item['url'] = self.allowed_domains[0] + sel.xpath('div/div/h2/a/@href').extract()[0]
			except:
				item['url'] = empty
			
			try:		
				desc0 = sel.xpath('div[@class="dateHeureEvent"]/a/text()').extract()[0]
				item['description'] = desc0
			except:
				item['description'] = empty

			try:
				item['location'] = sel.xpath('div[@class="author"]/div[@class="authorRight"]/a[2]/text()').extract()[0]
			except:
				item['location'] = empty

			
			item['latitude'] = empty
			item['longitude'] = empty

			try:
				item['price'] = sel.xpath("div/div[2]/div/text()").extract()[0].strip('\n').encode('utf-8').strip('€')
				item['currency'] = "€"
			except:
				item['price'] = empty
				item['currency'] = empty

			try:
				item['period'] = sel.xpath('div[@class="dateHeureEvent"]/a/text()').extract()[0]
			except:
				item['period'] = empty
			
			yield item
