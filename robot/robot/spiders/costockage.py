#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
from robot.country import France

class CostockageSpider(scrapy.Spider):
	name = "costockage"
	category = "storing"
	subcategory = "space"
	allowed_domains = ["https://www.costockage.fr"]
	France = France()
	cities = France.cities
	start_urls_0 = list(map(lambda x: "https://www.costockage.fr/garde-meuble/%s-5&plus-proche=10"%str(x), cities))
	start_urls = [url+"&"+"page="+str(x) for url in start_urls_0 for x in range(10)]

	def parse(self, response):
		for sel in response.xpath('//div[@itemtype="http://schema.org/Product"]'):
			item = AdItem()
		 	empty = ""
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath('@title').extract()[0]
			except:
				item['title'] = empty
			try:
				item['media'] = sel.xpath('div[1]/div[@class="customer_name_search"]/p/img/@src').extract()[0]
			except:
				item['media'] = empty
			try:
				item['url'] = sel.xpath('@id').extract()[0]
			except:
				item['url'] = empty
			try:
				item['description'] = sel.xpath('div[1]/div[@class="address"]/text()[2]').extract()[0]
			except:
				item['description'] = empty
			try:
				item['location']  = sel.xpath('div[1]/div[@class="address"]/a/text()').extract()[0]
				item['postal_code'] = int(item['location'].split('- ')[1])
			except:
				item['location'] = empty
                                item['postal_code'] = 0
			
			item['latitude'] = empty
			item['longitude'] = empty
			
			try:
				item['price'] = sel.xpath('div[3]/div[@class="price_div"]/div[@class="new_price"]/b/text()').extract()[0].encode('utf-8').split('€')[0]
				item['currency'] = "€"
			except:
				item['price'] = empty
				item['currency'] = empty

			try:	
				item['period'] = sel.xpath('div[3]/div[@class="price_div"]/div[@class="new_price"]/text()[2]').extract()[0].strip('/')
			except:
				item['period'] = empty 
			yield item
