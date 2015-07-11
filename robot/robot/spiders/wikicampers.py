#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import France

class SailsharingSpider(scrapy.Spider):
    name = "wikicampers"
    category = "moving"
    subcategory ="camping car"
    allowed_domains = ["http://www.wikicampers.fr"]
    # scrap zilok by categories
    France = France()
    cities = France.cities
    start_urls = list(map(lambda x: "http://www.wikicampers.fr/annonces-location-camping-car/"+str(x), cities))
    
    def parse(self, response):
        for sel in response.xpath('//div[@class="annonces"]'):
            item = AdItem()
            empty = ''
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath('div/h3/a/text()').extract()[0].strip("\n ")

            except:
                item['title'] = empty
            try:
                item['media'] = self.allowed_domains[0] + sel.xpath('div/a/img/@src').extract()[0].split('..')[-1]
            except:
                item['media'] = empty
            try:
                item['url'] = sel.xpath('div/a/@href').extract()[0]
            except:
                item['url'] = empty
            try:
                item['description'] = sel.xpath('div[@class="grid_inner annonce"]/p/text()').extract()[0].strip("\n ")

            except:
                item['description'] = empty
            try:
                item['location'] = sel.xpath('div/div[@class="city"]/text()').extract()[0].strip("\n ")

            except:
                item['location'] = empty
                        
            item['latitude'] = empty
            item['longitude'] = empty
            
            try:
                item['price'] = sel.xpath('div/span/text()').extract()[0].strip("\n ").split(' ')[0].encode('utf-8').strip('€')
                item['currency'] = "€"
            except:
                item['price'] = empty
                item['currency'] = empty
            
            try:
                item['period'] = sel.xpath('div/span/text()').extract()[0].strip("\n ").split(' ')[-1]
            except:
                item['period'] = empty

            yield item