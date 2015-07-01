#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import all_cities

class OuistockSpider(scrapy.Spider):
	name = "ouistock"
	category = "storing"
	subcategory ="space"
	allowed_domains = ["https://www.ouistock.fr"]
	# scrap by cities
	cities = all_cities()

	start_urls_0 = list(map(lambda x: "https://www.ouistock.fr/s/"+str(x), cities))
	start_urls = [url+"?page="+str(x) for url in start_urls_0 for x in range(100)]


	def parse(self, response):
		for sel in response.xpath('//ul[@id="results"]/li'):
			item = AdItem()
			empty = ''
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath('div[@class="resultContainer"]/div[@class="resultInfos"]/h3[@class="resultUserName"]/text()').extract()[0].strip('\n ')

			except: 
				item['title'] = empty

			try:	
				item['media'] = "https:"+sel.xpath('div[@class="resultContainer"]/div[@class="resultImgContainer"]/img/@src').extract()[0]
			except: 
				item['media'] = empty

			try:
				item['url'] = self.allowed_domains[0] + sel.xpath('div[@class="resultContainer"]/a/@href').extract()[0]
			except:
				item['url'] = empty
			
			try:		
				desc0 = sel.xpath('div[@class="resultContainer"]/div[@class="resultInfos"]/span[@class="resultType"]/text()').extract()[0].strip('\n ')
				desc1 = sel.xpath('div[@class="resultContainer"]/div[@class="resultInfos"]/span[@class="resultUsefull"]/text()').extract()[0].strip('\n ')

				item['description'] = desc0 + " "+ desc1
			except:
				item['description'] = empty

			try:
				item['location'] = sel.xpath('div[@class="resultContainer"]/div[@class="resultInfos"]/span[@class="resultUsefull"]/text()').extract()[0].strip('\n ').split(' ')[-1]

			except:
				item['location'] = empty
				
			item['latitude'] = empty
			item['longitude'] = empty

			try:
				item['price'] = sel.xpath('div[@class="resultContainer"]/div[@class="priceSpan"]/div[@class="innerSpan"]/i/text()').extract()[0].encode('utf-8').strip('\n €')
				item['currency'] = "€"
			except:
				item['price'] = empty
				item['currency'] = empty

			try:
				item['period'] = sel.xpath('div[@class="resultContainer"]/div[@class="priceSpan"]/div[@class="innerSpan"]/i/text()').extract()[0].strip("\n' /")

			except:
				item['period'] = empty
			
			yield item
