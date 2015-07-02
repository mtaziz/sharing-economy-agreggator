#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
#from robot.geoloc import geolocate

class BoaterflySpider(scrapy.Spider):
	name = "boaterfly"
	category = "leisure"
	subcategory = "boat"
	allowed_domains = ["http://www.boaterfly.com"]
	# scrap boaterfly by pages
	start_urls = list(map(lambda x: "http://www.boaterfly.com/fr/search?page="+str(x), range(1,21)))


	def parse(self, response):
		for sel in response.xpath('//li[@data-idx]'):
			item = AdItem()
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory
		 	empty = ""
		 	try:
				item['title'] = sel.xpath('div[3]/h3/a/text()').extract()[0]
			except:
				item['title'] = empty
			try:
				item['media'] = self.allowed_domains[0] + sel.xpath('div[2]/a/img/@src').extract()[0]
			except:
				item['media'] = empty
			try:
				item['url'] = sel.xpath('div[2]/a/@href').extract()[0]
			except:
				item['url'] = empty
			try:
				desc0 = sel.xpath('//li[@data-idx]/div[3]/p[@class="infos"]/span/text()').extract()[0]
				desc1 = sel.xpath('//li[@data-idx]/div[3]/p[@class="infos"]/span/strong/text()').extract()[0]
				desc2 = sel.xpath('//li[@data-idx]/div[3]/p[@class="infos"]/span[2]/text()').extract()[0]
				desc3 = sel.xpath('//li[@data-idx]/div[3]/p[@class="infos"]/span[2]/strong/text()').extract()[0]
				desc4 = sel.xpath('//li[@data-idx]/div[3]/p[@class="infos"]/span[3]/text()').extract()[0]
				desc5 = sel.xpath('//li[@data-idx]/div[3]/p[@class="infos"]/span[3]/strong/text()').extract()[0]

				item['description'] = desc0 + desc1+ " " + desc2 + desc3 + " " + desc4 + desc5
			except:
				item['description'] = empty
			try:
				item['location'] = sel.xpath('div[@class="box_details"]/h4[@class="location"]/text()').extract()[0]
				#result = geolocate(item['location'])
				#item['latitude'] = result['lat']
				#item['longitude'] = result['lng']
			except:
				item['location'] = empty
			item['latitude'] = empty
			item['longitude'] = empty
			try:
				item['price'] = sel.xpath('div[3]/div/p/text()').extract()[0].encode('utf-8').strip('€')
				item['currency'] = "€"
			except:
				item['price'] = empty
				item['currency'] = empty

			try:
				item['period'] = sel.xpath('div[3]/div[2]/span/text()').extract()[0]
			except:
				item['period'] = empty
			yield item
