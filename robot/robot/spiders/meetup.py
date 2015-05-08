#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import France

class MeetupSpider(scrapy.Spider):
    name = "meetup"
    category = "meet"
    subcategory = "events"
    allowed_domains = ["http://www.meetup.com"]
    # scrap by cities
    France = France()
    cities = France.cities
    
    start_urls_0 = list(map(lambda x: "http://www.meetup.com/cities/fr/"+str(x), cities))
    start_urls = [url+"/?pageToken=default|"+str(x) for url in start_urls_0 for x in [x * 100  for x in range(10)]]
    

    def parse(self, response):
        for sel in response.xpath('//ul[@data-view="card"]/li[@itemtype="http://schema.org/Organization"]'):
            item = AdItem()
            empty = ''
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath('div/a/text()').extract()[0]
            except: 
                item['title'] = empty

            try:    
                item['media'] = sel.xpath('div/a/@style').extract()[0].split('(')[-1].split(');')[0]

            except: 
                item['media'] = empty

            try:
                item['url'] = sel.xpath('div/a/@href').extract()[0]
            except:
                item['url'] = empty
            
            try:        
                item['description'] = sel.xpath('div/a/div[2]/p/text()').extract()[0]
            except:
                item['description'] = empty
            title = item['title']
            item['location'] = empty
            item['latitude'] = empty
            item['longitude'] = empty

            item['price'] = empty
            item['currency'] = empty
            item['period'] = empty
            
            yield item
