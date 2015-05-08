#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import France

class SupermarmiteSpider(scrapy.Spider):
    name = "supermarmite"
    category = "eating"
    subcategory = "meals"
    allowed_domains = ["http://www.super-marmite.com"]
    # scrap by cities
    France = France()
    cities = France.cities

    start_urls_0 = list(map(lambda x: "http://www.super-marmite.com/meals?where="+str(x), cities))
    start_urls = [url+"&page="+str(x) for url in start_urls_0 for x in range(10)]
    

    def parse(self, response):
        for sel in response.xpath('//ul[@class="users"]/li'):
            item = AdItem()
            empty = ''
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath('div/div[@class="content"]/h3[@class="orange"]/a/text()').extract()[0]
            except: 
                item['title'] = empty

            try:    
                item['media'] = sel.xpath('div/a/img/@src').extract()[0]
            except: 
                item['media'] = empty

            try:
                item['url'] = sel.xpath('div/div[@class="content"]/h3[@class="orange"]/a/@href').extract()[0]
            except:
                item['url'] = empty
            
            try:        
                item['description'] = sel.xpath('div/div[@class="content"]/p[@class="description"]/text()').extract()[0]
            except:
                item['description'] = empty

            try:
                item['location'] = sel.xpath('div/div[@class="content"]/div[@class="map_information"]/p/text()[2]').extract()[0]
            except:
                item['location'] = empty

            
            item['latitude'] = empty
            item['longitude'] = empty

            try:
                item['price'] = response.xpath('div/p[@class="price orange"]/text()').extract()[0].split('/')[0].encode('utf-8').strip('€')
                item['currency'] = "€"
            except:
                item['price'] = empty
                item['currency'] = empty
            try:
                item['period'] = response.xpath('div/div[@class="content"]/p[@class="meta"]/text()[3]').extract()[0]
            except:
                item['period'] = empty
            
            yield item
