#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import France

class MonsieurParkingSpider(scrapy.Spider):
	name = "monsieurparking"
	category = "parking"
	subcategory = "parking"
	allowed_domains = ["http://www.monsieurparking.com"]
	# scrap by cities
	France = France()
	geo_cities = France.geo
	cities = geo_cities.keys()
	start_urls = list(map(lambda x: "http://www.monsieurparking.com/location/"+str(x)+".html", cities))

	def parse(self, response):
		print response.url
		for sel in response.xpath("//div[@id='loginbox']"):
			item = AdItem()
			empty = ''
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath('div/div/div/div/p/a/text()').extract()[0]
				
			except: 
				item['title'] = empty

			try:
				item['location'] = response.url.split('/')[-1].split('.')[0]

			except:
				item['location'] = empty
			item['postal_code'] = 0
			try:	
				item['media'] = sel.xpath('div[@class="detail"]/img/@src').extract()[0]
			except: 
				item['media'] = self.allowed_domains[0] + "/images/parking-orange-26x26.png"

			try:
				item['url'] = self.allowed_domains[0] + sel.xpath("div/div/div/div/p/a/@href").extract()[0]
			except:
				item['url'] = empty
			
			try:		
				desc0 = sel.xpath('div/div/div/div/span/text()').extract()[0]
				desc1 = sel.xpath('div/div/div/div/span[2]/text()').extract()[0]
				item['description'] = desc0 + ", " + desc1
			except:
				item['description'] = empty
			try:
				item['latitude'] = float(self.geo_cities[item['location']]['lat'])
			except:
				item['latitude'] = empty

			try:
				item['longitude'] = float(self.geo_cities[item['location']]['lon'])
			except:
				item['longitude'] = empty
			try:
				item['price'] = sel.xpath("div/div/div/div/span[3]/text()").extract()[0].split('/')[0].encode('utf-8').split('€')[0]
				item['currency'] = "€"
			except:
				item['price'] = empty
				item['currency'] = empty
			try:
				item['period'] = sel.xpath("div/div/div/div/span[3]/text()").extract()[0].split('/')[1] 
			except:
				item['period'] = empty
			item['evaluations'] = empty			
			yield item
