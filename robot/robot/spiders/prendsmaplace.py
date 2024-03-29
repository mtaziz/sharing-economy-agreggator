#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import France
import re

class PrendsmaplaceSpider(scrapy.Spider):
    name = "prendsmaplace"
    category = "parking"
    subcategory = "parking"
    allowed_domains = ["http://www.prendsmaplace.fr"]
    pattern = re.compile('\d{2}')
    France = France()
    cities = France.cities
    geo = France.geo	
    start_urls = list(map(lambda x: "http://www.prendsmaplace.fr/page/%s/?s&geo-radius=100&geo-lat&geo-lng&categories=0&locations=0&dir-search=yes"%str(x), range(1,25)))

    def parse(self, response):
        for sel in response.xpath('//ul[@class="items"]/li'):
            item = AdItem()
            empty = ""
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath('div[@class="description"]/h3/a/text()').extract()[0]
            except:
                item['title'] =empty
            try:
                item['location'] = item['title'].split(' (')[0].split(' ')[-1]
            except:
                item['location'] = empty
            try:
                item['media'] = sel.xpath('div[@class="thumbnail"]/img/@src').extract()[0]
            except:
                item['media'] =empty
	    try:
                item['evaluations'] = sel.xpath('div[@class="thumbnail"]/div[@class="comment-count"]/text()').extract()[0]
            except:
                item['evaluations'] =empty

            try:
                item['url'] = sel.xpath('div[@class="description"]/h3/a/@href').extract()[0]
            except:
                item['url'] =empty
            try:
                item['description'] = sel.xpath('div[@class="description"]/text()[3]').extract()[0]
            except:
                item['description'] =empty
	    try:        
            	item['latitude'] = self.geo[item['location']]['lat']
	    except:
		item['latitude'] = empty
	    try:
                item['longitude'] = self.geo[item['location']]['lon']
            except:
                item['longitude'] = empty

            item['longitude'] = empty           
            item['price'] = empty
            item['currency'] = empty
            item['period'] = empty
	    try:
            	item['postal_code'] = re.search(self.pattern, item['title']).group()
	    except:
		item['postal_code'] = empty
            yield item
