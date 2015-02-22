import scrapy 
from boaterfly.items import BoaterflyItem

class BoaterflySpider(scrapy.Spider):
	name = "boaterfly"
	allowed_domains = ["http://www.boaterfly.fr"]
	# scrap boaterfly by pages
	start_urls = list(map(lambda x: "http://www.boaterfly.com/fr/search?page="+str(x), range(1,21)))


	def parse(self, response):
		for sel in response.xpath('//li[@data-idx]'):
			item = BoaterflyItem()
			item['title'] = sel.xpath('div[3]/h3/a/text()').extract()[0]
			
			item['media'] = sel.xpath('div[2]/a/img/@src').extract()[0]
			
			item['link'] = sel.xpath('div[2]/a/@href').extract()[0]
			
			#item['desc'] = sel.xpath('div[3]/p/span/text()').extract()[0] + response.xpath('div[3]/p/span/strong/text()').extract()[0]
			
			item['location'] = sel.xpath('div[3]/h4/text()').extract()[0]
			#item['distance'] = sel.xpath('td[3]/p[1]/text()').extract()
			item['price'] = sel.xpath('div[3]/div/p/text()').extract()[0]
			item['period'] = sel.xpath('div[3]/div[2]/span/text()').extract()[0]
			#item['owner'] = sel.xpath('td[4]/p[2]/text()').extract()
			yield item
