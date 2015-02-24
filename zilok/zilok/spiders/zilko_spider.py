import scrapy 
from zilok.items import ZilokItem

class ZilokSpider(scrapy.Spider):
	name = "zilok"
	allowed_domains = ["http://fr.zilok.com/"]
	start_urls = [
		"http://fr.zilok.com/location/a-paris"
	]

	def parse(self, response):
		for sel in response.xpath('//tr'):
			item = ZilokItem()
			item['title'] = sel.xpath('td[2]/h4/a/text()').extract()
			item['link'] = sel.xpath('td[2]/h4/a/@href').extract()
			item['desc'] = sel.xpath('td[2]/p/text()').extract()
			item['location'] = sel.xpath('td[3]/p[2]/strong/text()').extract()
			item['price'] = sel.xpath('td[4]/p[1]/strong/b/text()').extract()
			yield item