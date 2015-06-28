#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import France

class SharedparkingSpider(scrapy.Spider):
    name = "sharedparking"
    category = "parking"
    subcategory = "parking"
    allowed_domains = ["http://www.sharedparking.fr/"]
    France = France()
    cities = France.cities
    urls = list(map(lambda x: "http://www.sharedparking.fr/search?sc-cat=2&w="+str(x), cities))
    start_urls = [url+"&page="+str(i) for url in urls for i in range(3)]

    def parse(self, response):
        for sel in response.xpath('//table[@class="annonces"]/tr'):
            item = AdItem()
            empty = ""
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath('td/a/@title').extract()[0]

            except:
                item['title'] = empty
            
            item['media'] = empty
            
            try:
                item['url'] = self.allowed_domains[0] + sel.xpath('td/a/@href').extract()[0]
            except:
                item['url'] = empty
            try:
                item['description'] = sel.xpath('td[3]/text()').extract()[0]
            except:
                item['description'] = empty
            try:
                item['location'] = sel.xpath('td[2]/span/span/text()').extract()[0]
            except:
                item['location'] = empty
            
            item['latitude'] = empty
            item['longitude'] = empty
            
            try:
                price = sel.xpath('td[@style="text-align: right;"]/text()').extract()[0].split('/')
                item['price'] = price[0].encode('utf-8').strip('€')
                item['period'] = price[1]
                item['currency'] = "€"
            except:
                item['price'] = empty
                item['currency'] = empty
                item['period'] = empty
            
            yield item