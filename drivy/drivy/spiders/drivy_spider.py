import scrapy 
from drivy.items import DrivyItem

class DrivySpider(scrapy.Spider):
	name = "drivy"
	allowed_domains = ["https://www.drivy.com"]
	# scrap zilok by categories
	start_urls = list(map(lambda x: "https://www.drivy.com/search?page="+str(x), range(1,10)))


	def parse(self, response):
		for sel in response.xpath('//div[@data-car-id]'):
			item = DrivyItem()
			item['title'] = sel.xpath('div[2]/div[2]/a/@title').extract()
			
			item['media'] = sel.xpath('div[2]/div[1]/img/@src').extract()
			
			item['link'] = sel.xpath('div[2]/div[2]/a/@href').extract()
			
			item['desc'] = sel.xpath('div[2]/div[2]/div/text()').extract()
			
			item['location'] = sel.xpath('div[2]/div[2]/div[2]/text()[2]').extract()
			#item['distance'] = sel.xpath('td[3]/p[1]/text()').extract()
			item['price'] = sel.xpath('div[3]/text()').extract()
			item['period'] = sel.xpath('div[3]/span/text()').extract()
			#item['owner'] = sel.xpath('td[4]/p[2]/text()').extract()
			yield item
