#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime

class JelouemoncampingcarSpider(scrapy.Spider):
    name = "jelouemoncampingcar"
    category = "moving"
    subcategory = "camping car"
    allowed_domains = ["https://www.jelouemoncampingcar.com"]
    # scrap zilok by categories
    start_urls = list(map(lambda x: "https://www.jelouemoncampingcar.com/louer-un-camping-car-entre-particuliers/?page="+str(x), range(1,77)))

    def parse(self, response):
        for sel in response.xpath('//div[@class="card"]'):
            item = AdItem()
            empty = ''
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath('div[@class="content"]/div[@class="vehicle-info"]/p/text()').extract()[0]
            except:
                item['title'] = empty
            try:
                item['media'] = sel.xpath('a/div[@class="image"]/img/@src').extract()[0]
            except:
                item['title'] = empty
            try:
                item['url'] = self.allowed_domains[0] + sel.xpath('a/@href').extract()[0]
            except:
                item['url'] = empty
            try:
                item['description'] = sel.xpath('div[@class="content"]/div[@class="vehicle-info"]/p[@class="description"]/text()').extract()[0].strip("\n ")
            except:
                item['description'] = empty
            try:
                item['location'] = sel.xpath('div[@class="content"]/div[@class="vehicle-info"]/p[@class="city"]/strong/@title').extract()[0]
            except:
                item['location'] = empty

            item['latitude'] = empty
            item['longitude'] = empty
            
            try:
                item['price'] = sel.xpath('a/div[@class="image"]/span[@class="price"]/strong/text()').extract()[0].encode('utf-8').strip('€')
                item['currency'] = "€"
            except:
                item['price'] = empty
                item['currency'] = empty

            item['period'] = "jour"
            

            yield item