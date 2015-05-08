#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem

class ZilokSpider(scrapy.Spider):
	name = "zilok"
	category = "daily"
	subcategory = "brico"
	allowed_domains = ["http://www.zilok.fr"]
	# scrap boaterfly by pages
	start_urls = ["http://fr.zilok.com/apiv2/index.php/item/search/api/?action=item.search&api_key=akaka12JHKLAs455saasasa54sJLJLA&distance=20000&&language=2&lat=48.857&limit=10000&lng=2.351&order=item_rating_number&real_search=1&offset=0"]

	def parse(self, response):
		for sel in response.xpath('//item[@id]'):
			item = AdItem()
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory
		 	empty = ""
		 	try:
				item['title'] = sel.xpath('title/text()').extract()[0]
			except:
				item['title'] = empty
			try:
				item['media'] = sel.xpath('image/palm/@url').extract()[0]
			except:
				item['media'] = empty
			try:
				item['url'] = sel.xpath('link/text()').extract()[0]
			except:
				item['url'] = empty
			try:
				item['description'] = sel.xpath('subtitle/text()').extract()[0]
			except:
				item['description'] = empty
			try:
				item['location'] = sel.xpath('location/locality/text()').extract()[0]
			except:
				item['location'] = empty
			item['latitude'] = empty
			item['longitude'] = empty
			try:
				item['price'] = sel.xpath('price/text()').extract()[0].encode('utf-8').strip('€')
				item['currency'] = "€"
			except:
				item['price'] = empty
				item['currency'] = empty

			item['period'] = empty
			yield item
