import scrapy 
from drivy.items import DrivyItem
import datetime

class DrivySpider(scrapy.Spider):
	name = "drivy"
	category = "moving"
	allowed_domains = ["https://www.drivy.com"]
	# scrap zilok by categories
	start_urls = list(map(lambda x: "https://www.drivy.com/search?page="+str(x), range(1,52)))


	def parse(self, response):
		for sel in response.xpath('//div[@data-car-id]'):
			item = DrivyItem()
			item['source'] = self.name
			item['category'] = self.category
			item['creation_date'] = datetime.datetime.now()
			item['title'] = sel.xpath('div[2]/div[2]/a/@title').extract()[0]
			
			item['media'] = sel.xpath('div[2]/div[1]/img/@src').extract()[0]
			
			item['link'] = sel.xpath('div[2]/div[2]/a/@href').extract()[0]
			
			item['desc'] = sel.xpath('div[2]/div[2]/div/text()').extract()[0]
			
			item['location'] = sel.xpath('div[2]/div[2]/div[2]/text()[2]').extract()[0]
			#item['distance'] = sel.xpath('td[3]/p[1]/text()').extract()
			item['price'] = sel.xpath('div[3]/text()').extract()[0]
			item['period'] = sel.xpath('div[3]/span/text()').extract()[0]
			#item['owner'] = sel.xpath('td[4]/p[2]/text()').extract()
			yield item
