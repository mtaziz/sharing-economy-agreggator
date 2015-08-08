#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
from robot.country import France

class ZilokSpider(scrapy.Spider):
	name = "zilok"
	category = "daily"
	subcategory = "brico"
	allowed_domains = ["http://www.zilok.fr"]
	France = France()
	cities = France.geo
	start_urls = []
	for k,v in cities.items():
		url = "http://fr.zilok.com/apiv2/index.php/item/search/api/?action=item.search&api_key=akaka12JHKLAs455saasasa54sJLJLA&distance=15000&language=2&lat="+str(v["lat"])+"&limit=1000&lng="+str(v["lon"])+"&real_search=1&where="+k  
		start_urls.append(url)
	#start_urls = list(map(lambda x:"http://fr.zilok.com/apiv2/index.php/item/search/api/?action=item.search&api_key=akaka12JHKLAs455saasasa54sJLJLA&distance=15000&language=2&lat=%s&limit=30&lng=%s&real_search=1&where=%s"%(_geo[x]["lat"], _geo[x]["lon"], x), cities))
	print start_urls
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
			try:
				item['postal_code'] = sel.xpath('location/postal_code/text()').extract()[0]
			except:
				item['postal_code'] = empty
			try:
				item['latitude'] = sel.xpath('location/lat/text()').extract()[0] if len(sel.xpath('location/lat/text()').extract()[0]) > 1 else sel.xpath('/search/lat/text()').extract()[0]
			except:
				item['latitude'] = empty
			try:	
				item['longitude'] = sel.xpath('location/lng/text()').extract()[0] if len(sel.xpath('location/lng/text()').extract()[0]) > 1 else sel.xpath('/search/lng/text()').extract()[0] 
			except:
				item['longitude'] = empty
			try:
				item['price'] = sel.xpath('price/text()').extract()[0]
			except:
				item['price'] = empty
			try:
				item['currency'] = sel.xpath('price/@currency').extract()[0]
			except:
				item['currency'] = empty
			try:	
				item['evaluations'] = sel.xpath('evaluation_number/text()').extract()[0]
			except:
				item['evaluations'] = empty
			item['period'] = "jour"
			yield item
