import scrapy 
from robot.items import AdItem
import datetime

class HousetripSpider(scrapy.Spider):
	name = "housetrip"
	category = "housing"
	allowed_domains = ["http://www.housetrip.fr"]
	# scrap zilok by categories
	cities = ['paris', 'nantes', 'lille', 'bordeaux', 'nancy', 'nice']
	start_urls_0 = list(map(lambda x: "http://www.housetrip.fr/fr/rechercher/"+str(x), cities))
	start_urls = [url+"?page="+str(x) for url in start_urls_0 for x in range(100)]
	

	def parse(self, response):
		for sel in response.xpath('//div[@data-element-id]'):
			item = AdItem()
			item['source'] = self.name
			item['category'] = self.category
			item['title'] = sel.xpath('div[2]/h3/a/text()').extract()[0]
			item['media'] = sel.xpath('div[1]/@style').extract()[0].split('(')[1].split(')')[0]
			item['url'] = sel.xpath('div[2]/h3/a/@href').extract()[0]
			desc0 = sel.xpath('div[2]/div/ul[1]/li[1]/text()').extract()[0]
			desc1 = sel.xpath('div[2]/div/ul[1]/li[2]/text()').extract()[0]
			desc2 = sel.xpath('div[2]/div/ul[2]/li/text()').extract()[0]
			item['description'] = desc0 + " " + desc1 + " " + desc2
			item['location'] = sel.xpath('div[2]/h4/text()').extract()[0]
			item['price'] = sel.xpath('div[3]/div/p/text()').extract()[0]
			item['period'] = sel.xpath('div[3]/div/p[2]/text()').extract()[0]
			
			yield item
