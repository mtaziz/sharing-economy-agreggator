#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime

class SailsharingSpider(scrapy.Spider):
    name = "sailsharing"
    category = "leisure"
    subcategory = "boat"
    allowed_domains = ["http://www.sailsharing.com"]
    # scrap zilok by categories
    start_urls = list(map(lambda x: "http://www.sailsharing.com/fr/location-bateau/search?page="+str(x), range(1,36)))


    def parse(self, response):
        for sel in response.xpath('//div[@class="block"]'):
            item = AdItem()
            empty = ''
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath('div/h2/a/text()').extract()[0].strip("\n ")

            except:
                item['title'] = empty
            try:
                item['media'] = self.allowed_domains[0] + sel.xpath('a/img/@src').extract()[0]
            except:
                item['media'] = empty
            try:
                item['url'] = self.allowed_domains[0] + sel.xpath('a/@href').extract()[0]
            except:
                item['url'] = empty
            try:
                item['description'] = sel.xpath('div/div[@class="boat-info"]/text()').extract()[0].strip("\n ")

            except:
                item['description'] = empty
            try:
                item['location'] = sel.xpath('div/div/h4/strong/text()').extract()[0]
            except:
                item['location'] = empty
                        
            item['latitude'] = empty
            item['longitude'] = empty
            
            try:
                item['price'] = sel.xpath('div[@class="hosting-meta"]/div/span/strong/text()').extract()[0].encode('utf-8').strip('€')
                item['currency'] = '€'
            except:
                item['price'] = empty
                item['currency'] = empty
            
            try:
                item['period'] = sel.xpath('div[3]/span/text()').extract()[0]
            except:
                item['period'] = empty

            yield item