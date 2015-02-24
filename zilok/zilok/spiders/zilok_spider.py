import scrapy 
from zilok.items import ZilokItem

class ZilokSpider(scrapy.Spider):
	name = "zilok"
	allowed_domains = ["http://fr.zilok.com/"]
	# scrap zilok by categories
	start_urls = [
		"http://fr.zilok.com/c-200100000-location/outils",
		"http://fr.zilok.com/c-200200000-location/jardinage",
		"http://fr.zilok.com/c-200400000-location/manutention",
		"http://fr.zilok.com/c-500700000-location/velo"
	]

	def parse(self, response):
		for sel in response.xpath('//tr'):
			item = ZilokItem()
			item['title'] = sel.xpath('td[2]/h4/a/text()').extract()
			item['media'] = sel.xpath('td[1]/span/img/@src').extract()
			item['link'] = sel.xpath('td[2]/h4/a/@href').extract()
			item['desc'] = sel.xpath('td[2]/p/text()').extract()
			item['location'] = sel.xpath('td[3]/p[2]/strong/text()').extract()
			item['distance'] = sel.xpath('td[3]/p[1]/text()').extract()
			item['price'] = sel.xpath('td[4]/p[1]/strong/b/text()').extract()
			item['period'] = sel.xpath('td[4]/p[1]/text()').extract()
			item['owner'] = sel.xpath('td[4]/p[2]/text()').extract()
			yield item