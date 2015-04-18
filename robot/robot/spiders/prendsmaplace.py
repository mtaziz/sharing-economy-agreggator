#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime

class DrivySpider(scrapy.Spider):
    name = "prendsmaplace"
    category = "storing"
    subcategory = "parking"
    allowed_domains = ["http://www.prendsmaplace.fr"]
    # scrap zilok by categories
    start_urls = list(map(lambda x: "http://www.prendsmaplace.fr/page/%s/?s&geo-radius=100&geo-lat&geo-lng&categories=0&locations=0&dir-search=yes"%str(x), range(1,25)))


    def parse(self, response):
        for sel in response.xpath('//ul[@class="items"]/li'):
            item = AdItem()
            empty = "unknown"
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath('div[@class="description"]/h2/text()').extract()[0]

            except:
                item['title'] =empty
            try:
                item['media'] = sel.xpath('div[@class="thumbnail"]/img/@src').extract()[0]
            except:
                item['media'] =empty
            try:
                item['url'] = sel.xpath('div[@class="description"]/h3/a/@href').extract()[0]
            except:
                item['url'] =empty
            try:
                item['description'] = sel.xpath('div[@class="description"]/text()[3]').extract()[0]
            except:
                item['description'] =empty
            
            item['location'] =empty            
            item['latitude'] = empty
            item['longitude'] = empty           
            item['price'] = empty
            
            item['period'] = empty
         
            yield item