#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime


class EloueMotoSpider(scrapy.Spider):
    name = "elouemoto"
    category = "moving"
    subcategory = "moto"
    allowed_domains = ["https://www.e-loue.com"]
    # scrap zilok by categories
    start_urls = list(map(lambda x: "https://www.e-loue.com/location/auto-et-moto/scooter/125-cc/page/"+str(x), range(1,100)))


    def parse(self, response):
        for sel in response.xpath('//ol[@class="product-layout"]/li'):
            item = AdItem()
            empty = "unknown"
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath("@name").extract()[0]
            except:
                print("scraping fails")
            try:
                item['media'] = sel.xpath('div/div/a/img/@style').extract()[0].split(')')[0].split(':')[-1]

            except:
                print("scraping fails")
            try:
                item['url'] = sel.xpath('div/div/a/@href').extract()[0]
            except:
                print("scraping fails")
            try:
                item['description'] = sel.xpath('div/div[@class="info"]/p[@class="full_description"]/text()').extract()[0]

            except:
                print("scraping fails")
            try:
                item['location'] = sel.xpath('div/div[@class="info"]/p[@class="full_description"]/text()').extract()[0]
            except:
                print("scraping fails")
            
            item['latitude'] = sel.xpath("@locationx").extract()[0]
            item['longitude'] = sel.xpath("@locationy").extract()[0]
            
            try:
                price = sel.xpath('div/div/span[@class="badge price"]/text()').extract()[0].split('/')

                item['price'] = price[0].strip(' ').encode('utf-8').strip('€')
                item['period'] = price[1]
            except:
                print("scraping fails")
            
            yield item