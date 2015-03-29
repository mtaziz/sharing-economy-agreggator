#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime

class OwlcampSpider(scrapy.Spider):
	name = "owlcamp"
	category = "moving"
	subcategory = "camping"
	allowed_domains = ["http://owlcamp.com"]
	# scrap zilok by categories
	start_urls = list(map(lambda x: "http://owlcamp.com/fre/gardens/all/page:%s" % str(x), range(2,15)))
	start_urls.append("http://owlcamp.com/fre/gardens/all")

	def parse(self, response):
		for sel in response.xpath('//div[@class="garden-card"]'):
			item = AdItem()
			empty = "unknown"
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath('div[@class="garden-card__location"]/text()').extract()[0].strip(' ')
			except:
				item['title'] = empty
			try:
				item['media'] = self.allowed_domains[0] + sel.xpath('a[@rel]/img/@src').extract()[0]
			except:
				item['media'] = empty
			try:
				item['url'] = self.allowed_domains[0] + sel.xpath('a[@rel]/@href').extract()[0]
			except:
				item['url'] = empty
			try:
				item['description'] = sel.xpath('div[@class="garden-card__location"]/text()').extract()[0].strip(' ')
			except:
				item['description'] = empty
			try:
				item['location'] = sel.xpath('div[@class="garden-card__location"]/text()').extract()[0].strip(' ')
			except:
				item['location'] = empty

			item['latitude'] = empty
			item['longitude'] = empty

			try:
				price = sel.xpath('div[@class="garden-card__price"]/div/text()').extract()[0].strip(' ')
				if price == "gratuit":
					item['price'] = 0
				else:
					item['price'] = price.split('/')[0]
					item['period'] = price.split('/')[-1]		
			except:
				item['price'] = empty
				item['period'] = empty

			yield item