#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime

class MeetupSpider(scrapy.Spider):
    name = "meetnsport"
    category = "meet"
    subcategory = "training"
    allowed_domains = ["http://www.meetnsport.com"]
    
    start_urls = list(map(lambda x: "http://www.meetnsport.com/index.php?option=com_community&view=events&task=display&Itemid=111&limitstart=%s"%str(x), [l*20 for l in range(50)]))
    

    def parse(self, response):
        for sel in response.xpath('//div[@class="community-events-results-item"]'):
            item = AdItem()
            empty = ''
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath('div[@class="community-events-results-right"]/h3/a/strong/text()').extract()[0]
            except: 
                item['title'] = empty

            try:    
                item['media'] = sel.xpath('div[@class="community-events-results-left"]/a/img/@src').extract()[0]

            except: 
                item['media'] = empty

            try:
                item['url'] = self.allowed_domains[0] + sel.xpath('div[@class="community-events-results-left"]/a/@href').extract()[0]
            except:
                item['url'] = empty
            
            try:        
                start = "De " + sel.xpath('div[@class="community-events-results-right"]/div[@class="eventTime"]/text()').extract()[0]
                end = "a " + sel.xpath('div[@class="community-events-results-right"]/div[@class="eventTime"]/text()[2]').extract()[0]

                item['description'] = start + ' ' + end
                item['period'] = item['description']
            except:
                item['description'], item['period'] = empty, empty

            try:
                item['location'] = xpath('div[@class="community-events-results-right"]/div[@class="eventLocation"]/text()').extract()[0]
            except:
                item['location'] = empty

            item['latitude'] = empty
            item['longitude'] = empty
            item['price'] = empty

            yield item
