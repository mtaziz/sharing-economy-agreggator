#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime

class CohebergementSpider(scrapy.Spider):
    name = "cohebergement"
    category = "housing"
    subcategory = "room"
    allowed_domains = ["http://www.cohebergement.com"]
    # scrap zilok by categories
    start_urls = list(map(lambda x: "http://www.cohebergement.com/location/c/3-france?page="+str(x), range(1,100)))


    def parse(self, response):
        for sel in response.xpath('//div[@class="row"]'):
            item = AdItem()
            empty = "unknown"
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath("div[2]/h2/a/text()").extract()[0]
            except:
                item['title'] = empty
            try:
                item['media'] = self.allowed_domains[0] + sel.xpath('div/a/img/@src').extract()[0]
            except:
                item['media'] = empty
            try:
                item['url'] = self.allowed_domains[0] + sel.xpath('div[2]/p/a/@href').extract()[0]
            except:
                item['url'] = empty
            try:
                item['description'] = sel.xpath('div[2]/p/text()').extract()[0]
            except:
                item['description'] = empty
            try:
                item['location'] = sel.xpath('div[2]/text()[3]').extract()[0]
            except:
                item['location'] = empty
            
            item['latitude'] = empty
            item['longitude'] = empty
            
            try:
                item['price'] = sel.xpath('div[3]/div/span/text()').extract()[0].encode('utf-8').strip('€')
                item['currency'] = "€"
            except:
                item['price'] = empty
                item['currency'] = empty
            
            item['period'] = empty
            
            yield item