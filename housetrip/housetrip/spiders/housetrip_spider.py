import scrapy 
from housetrip.items import HousetripItem
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
			item = HousetripItem()
			item['source'] = self.name
			item['category'] = self.category
			item['creation_date'] = datetime.datetime.now()
			item['title'] = sel.xpath('div[2]/h3/a/text()').extract()[0]
			
			item['media'] = sel.xpath('div[1]/@style').extract()[0].split('(')[1].split(')')[0]
			
			item['link'] = sel.xpath('div[2]/h3/a/@href').extract()[0]
			
			#item['desc'] = sel.xpath('div[2]/div[2]/div/text()').extract()
			
			item['location'] = sel.xpath('div[2]/h4/text()').extract()[0]
			#item['distance'] = sel.xpath('td[3]/p[1]/text()').extract()
			item['price'] = sel.xpath('div[3]/div/p/text()').extract()[0]
			item['period'] = sel.xpath('div[3]/div/p[2]/text()').extract()[0]
			yield item
