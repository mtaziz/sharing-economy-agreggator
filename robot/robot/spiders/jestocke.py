import scrapy 
from robot.items import AdItem

class JestockeSpider(scrapy.Spider):
	name = "jestocke"
	category = "storing"
	allowed_domains = ["http://www.jestocke.fr"]
	# scrap boaterfly by pages
	start_urls = list(map(lambda x: "https://www.jestocke.com/location/recherche/"+str(x), range(51)))


	def parse(self, response):
		for sel in response.xpath('//article'):
			item = AdItem()
			item['source'] = self.name
			item['category'] = self.category
			item['title'] = sel.xpath('div[2]/h2/a/text()').extract()[0]
			item['media'] = sel.xpath('div[1]/a/@href').extract()[0]
			item['url'] = sel.xpath('div[2]/h2/a/@href').extract()[0]
			item['description'] = sel.xpath('div[2]/p/text()').extract()[0]
			item['location']  = sel.xpath('div[2]/p[2]/text()').extract()[0]
			item['latitude']  = sel.xpath('div[2]/p[3]/a/span[@class="latitude"]/text()').extract()[0]
			item['longitude'] = sel.xpath('div[2]/p[3]/a/span[@class="longitude"]/text()').extract()[0]
			item['price'] = sel.xpath('div[3]/div/div/span[@class="price-figure"]/text()').extract()[0]
			item['price_unit'] = sel.xpath('div[3]/div/div/span[@class="bloc-price_units"]/text()').extract()[0]
			item['period'] = sel.xpath('div[3]/div/div/text()').extract()[0]
			yield item
