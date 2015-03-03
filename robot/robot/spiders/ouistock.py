import scrapy 
from robot.items import AdItem
import datetime
from geopy.geocoders import Nominatim 

class OuistockSpider(scrapy.Spider):
	name = "ouistock"
	category = "storing"
	allowed_domains = ["https://www.ouistock.fr"]
	# scrap zilok by categories
	cities = ['paris--france', 'nantes--france', 'lille--france', 'bordeaux--france', 'nancy--france', 'nice--france']
	start_urls_0 = list(map(lambda x: "https://www.ouistock.fr/s/"+str(x), cities))
	start_urls = [url+"?page="+str(x) for url in start_urls_0 for x in range(100)]
	

	def parse(self, response):
		for sel in response.xpath('//ul[@id="results"]/li'):
			item = AdItem()
			empty = 'unknown'
			item['source'] = self.name
			item['category'] = self.category
			try:
				item['title'] = sel.xpath("div/div[@class='resultInfos']/span[@class='resultType']/text()").extract()[0].strip('\n ')

			except: 
				item['title'] = empty

			try:	
				item['media'] = sel.xpath('div/div[@class="resultImgContainer"]/img/@src').extract()[0]
			except: 
				item['media'] = empty

			try:
				item['url'] = sel.xpath('div/a/@href').extract()[0]
			except:
				item['url'] = empty
			
			try:		
				item['description'] = sel.xpath('div/div[@class="resultInfos"]/span[@class="resultUsefull"]/text()').extract()[0]
			except:
				item['description'] = empty

			item['location'] = empty
			item['latitude'] = location.latitude
			item['longitude'] = location.longitude

			try:
				item['price'] = sel.xpath('div/div[@class="priceSpan"]/div/i/text()"').extract()[0]
			except:
				item['price'] = empty

			try:
				item['period'] = sel.xpath("div/div[@class='priceSpan']/div/span/text()").extract()[0].strip("\n' /")

			except:
				item['period'] = empty
			
			yield item
