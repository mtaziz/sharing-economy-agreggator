#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import searchZip
import re
from robot.country import France

class ParkadomSpider(scrapy.Spider):
    name = "parkadom"
    category = "parking"
    subcategory = "parking"
    allowed_domains = ["http://www.parkadom.com"]
    #start_urls = list(map(lambda x: "http://www.parkadom.com/location-parking/resultat-de-recherche?page"+str(x), range(1,52)))
    start_urls = ["http://www.parkadom.com/location-parking/resultat-de-recherche?group=100"]
    pattern = re.compile("\d{1,}")
    France = France()
    geo = France.geo

    def parse(self, response):
        for sel in response.xpath('//div[@class="box-parking-dispo"]'):
            item = AdItem()
            empty = ""
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath('div/span[@class="title-parking"]/text()').extract()[0]
		item['postal_code'] = searchZip(item['title'])
            except:
                item['title'] = empty
		item['postal_code'] = 0
            try:
                item['media'] = self.allowed_domains[0] + sel.xpath('div/div/div[@class="detail-parking-left"]/div/img/@src').extract()[0]
            except:
                item['media'] = empty
            try:
                item['url'] = self.allowed_domains[0] + sel.xpath('div/div/div[@class="detail-parking-right"]/div[2]/a/@href').extract()[0]
            except:
                item['url'] = empty
            try:
                item['description'] = sel.xpath('div/div/div[@class="detail-parking-left"]/div/img/@alt').extract()[0]
            except:
                item['description'] = empty
            try:
                item['location'] = sel.xpath('div/div/div/div/h1/span/text()').extract()[0]
            except:
                item['location'] = empty
	    try:            
            	item['latitude'] = self.geo[item['location'].split(',')[-2].strip(' ')]['lat']
	    except:
		item['latitude'] = empty
            try:
		
		item['longitude'] = self.geo[item['location'].split(',')[-2].strip(' ')]['lon']
	    except:
	        item['longitude'] = empty
            
            try:
                item['price'] = sel.xpath('div/div/div[@class="detail-parking-right"]/div/span/span/text()').extract()[0].encode('utf-8').strip('€')
                item['currency'] = "€"
            except:
                item['price'] = empty
                item['currency'] = empty
            
            try:
                item['period'] = sel.xpath('div/div/div[@class="detail-parking-right"]/div/span/text()').extract()[0].strip('/')
            except:
                item['period'] = empty
	    try:
                item['evaluations'] = re.search(self.pattern, sel.xpath('div/div/div[@class="detail-parking-left"]/div/div/span/text()').extract()[0]).group()
            except:
                item['evaluations'] = empty

		
            yield item
