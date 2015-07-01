#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import all_cities

class PrendsmaplaceSpider(scrapy.Spider):
    name = "prendsmaplace"
    category = "parking"
    subcategory = "parking"
    allowed_domains = ["http://zenpark.com"]
    cities = all_cities()
    start_urls = list(map(lambda x: "http://zenpark.com/parkings?subscribe=False&address="+str(x), cities))

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
                item['location'] = self.France.city_from_title(item['title'])
            except:
                item['location'] = empty
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
            
            item['latitude'] = empty
            item['longitude'] = empty           
            item['price'] = empty
            item['currency'] = empty
            item['period'] = empty
         
            yield item