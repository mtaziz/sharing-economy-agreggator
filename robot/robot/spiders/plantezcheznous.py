#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import searchZip

class HousetripSpider(scrapy.Spider):
	name = "plantezcheznous"
	category = "eating"
	subcategory = "gardens"
	allowed_domains = ["http://www.plantezcheznous.com"]
	pages = 18*range(1,1000)
	start_urls = list(map(lambda x: "http://www.plantezcheznous.com/annonce-potager-a-partager.html,"+str(x), pages))

	def parse(self, response):
		for sel in response.xpath('//div[@class="ligne_simple"]'):
			item = AdItem()
			empty = ''
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath('div[@class="annonce_detail"]/p/a/@title').extract()[0]
			except: 
				item['title'] = empty

			try:	
				item['media'] = sel.xpath('div[@class="annonce_img"]/a/img/@src').extract()[0]
			except: 
				item['media'] = empty

			try:
				item['url'] = sel.xpath('div[@class="annonce_img"]/a/@href').extract()[0]
			except:
				item['url'] = empty
			
			try:		
				item['description'] = sel.xpath('div[@class="annonce_detail"]/span[@class="desc"]/a/text()[2]').extract()[0]
			except:
				item['description'] = empty

			try:
				item['location'] = sel.xpath('div[@class="annonce_detail"]/span[@class="desc"]/a/span/text()').extract()[0]
			except:
				item['location'] = empty

			try:
                                item['postal_code'] = searchZip(sel.xpath('div[@class="annonce_detail"]/span[@class="desc"]/a/span[2]/text()').extract()[0])
                        except:
                                item['postal_code'] = empty			
			item['latitude'] = empty
			item['longitude'] = empty
			item['price'] = empty
			item['currency'] = empty

			try:
				item['period'] = sel.xpath('div[@class="annonce_detail"]/span[@class="desc"]/a/text()[2]').extract()[0].split('-')[0]
			except:
				item['period'] = empty
			item['evaluations'] = empty			
			yield item
