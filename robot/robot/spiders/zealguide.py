#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime

class EloueBricoSpider(scrapy.Spider):
    name = "zealguide"
    category = "leisure"
    subcategory = "visiting"
    allowed_domains = ["https://www.zealguide.com"]
    start_urls = ["https://www.zealguide.com/fr?q=france&transaction_type=offering&view=list"]


    def parse(self, response):
        for sel in response.xpath("//div[@class='home-list-item']"):
            item = AdItem()
            empty = ""
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath("div[2]/h2/a/text()").extract()[0]
            except:
                item['title'] = empty
            
            try:
                item['media'] = sel.xpath('a/img/@src').extract()[0]
            except:
                item['media'] = empty
            
            try:
                item['url'] = self.allowed_domains[0] + sel.xpath('a/@href').extract()[0]
            except:
                item['url'] = empty
            
            try:
                item['description'] = sel.xpath('div[3]/div[2]/a/text()').extract()[0]

            except:
                item['description'] = empty
            
            item['location'] = empty
            
            item['latitude'] = empty
            item['longitude'] = empty
            
            try:
                item['price'] = sel.xpath('div/div/div/text()').extract()[0].encode('utf-8').strip('€')
            except:
                item['price'] = empty
            
            item['period'] = "day"
            yield item

