#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import France
import requests
import json

class BandbikeSpider(scrapy.Spider):
    name = "bandbike"
    category = "moving"
    subcategory = "velo"
    allowed_domains = ["http://bandbike.com"]
    start_urls = []    
    France = France()
    geo = France.geo
    cities = geo.keys()
    for city in cities:
    	url = "http://bandbike.com/ref/city/"+ city
	req = requests.get(url=url)
        res = json.loads(req.text)
	for r in res:
	    url = "http://bandbike.com/ad/search?terms=%s+(%s)&searchCityId=%s"%(r['name'],r['zipcode'], r['id'])
	    urls = [url+"&currentPage="+str(x) for x in xrange(1,10)]
	    start_urls += urls 
    
    #print start_urls
    def parse(self, response):
        for sel in response.xpath('//div[@class="row"]'):
			item = AdItem()
			empty = ""
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath("div/div/div/h4/text()").extract()[0]
			except:
				item['title'] = empty
			try:
				item['media'] = sel.xpath('div/div/div/img/@src').extract()[0]

			except:
				item['media'] = empty
			try:
				item['url'] = self.allowed_domains[0] + sel.xpath('div/div/div/a/@href').extract()[0]
			except:
				item['url'] = empty
			try:
				item['description'] = sel.xpath('div/div/div/div/div/h5/text()').extract()[0]

			except:
				item['description'] = empty
			
			item['location'] = response.url.split('terms=')[1].split('+')[0]
			item['postal_code'] = response.url.split('terms=')[1].split('+')[1].split(')')[0].strip('(')
			item['evaluations'] = empty
			
			try:
				item['latitude'] = float(self.geo[item['location']]['lat'])
			except:
				item['latitude'] = empty

			try:
				item['longitude'] = float(self.geo[item['location']]['lon'])
			except:
				item['longitude'] = empty

			try:
				price = sel.xpath('div/div/div/div/div[3]/h5/text()').extract()[0].split('/')
				item['price'] = price[0].strip(' ').encode('utf-8').strip('€')
				item['period'] = price[1]
				item['currency'] = "€"
			except:
				item['price'] = empty
				item['period'] = empty
				item['currency'] = empty
			yield item
