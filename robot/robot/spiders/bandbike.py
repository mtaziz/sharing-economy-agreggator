#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime


class BandbikeSpider(scrapy.Spider):
    name = "bandbike"
    category = "moving"
    subcategory = "velo"
    allowed_domains = ["http://bandbike.com/"]
    # scrap zilok by categories
    start_urls = list(map(lambda x: "http://bandbike.com/ad/search?terms=Paris+%s+(7500%s)&searchCityId=29617&categoryFacetId=" %(str(x),str(x)), range(1,20)))
    
    def parse(self, response):
        for sel in response.xpath('//div[@class="row"]'):
			item = AdItem()
			empty = "unknown"
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath("div/div/div/h4/text()").extract()[0]
			except:
				item['title'] = empty
			try:
				item['media'] = sel.xpath('div/div/div/img/@src').extract()[0]

			except:
				item['media'] = empty
			try:
				item['url'] = self.allowed_domains[0] + sel.xpath('div/div/div/a/@href').extract()[0]
			except:
				item['url'] = empty
			try:
				item['description'] = sel.xpath('div/div/div/h4/text()').extract()[0]

			except:
				item['description'] = empty
			
			item['location'] = empty
			item['latitude'] = empty
			item['longitude'] = empty

			try:
				price = sel.xpath('div/div/div/div/div[3]/h5').extract()[0].split('/')
				item['price'] = price[0].strip(' ').encode('utf-8').strip('€')
				item['period'] = price[1]
			except:
				item['price'] = empty
				item['period'] = empty

			yield item