#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import France

class EloueBricoSpider(scrapy.Spider):
    name = "eloue"
    category = "daily"
    subcategory = "brico"
    allowed_domains = ["https://www.e-loue.com"]
    # scrap zilok by categories
    start_urls0 = list(map(lambda x: "https://www.e-loue.com/location/page/%s/?r=9"%str(x), range(1,20)))
    France = France()
    cities = France.cities
    start_urls= [url+'&l='+city for url in start_urls0 for city in cities ]

    def parse(self, response):
        for sel in response.xpath('//ol[@class="product-layout"]/li'):
            item = AdItem()
            empty = ""
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath("@name").extract()[0]
            except:
                item['title'] = empty
            try:
                item['media'] = "https:"+sel.xpath('div/div/a/img/@style').extract()[0].split(')')[0].split(':')[-1]

            except:
                item['media'] = empty
            try:
                item['url'] = self.allowed_domains[0] + sel.xpath('div/div/a/@href').extract()[0]
            except:
                item['url'] = empty
            try:
                item['description'] = sel.xpath('div/div[@class="info"]/p[@class="full_description"]/text()').extract()[0]

            except:
                item['description'] = empty
            try:
                item['location'] = sel.xpath('div/div[@class="info"]/p/text()').extract()[0]
            except:
                item['location'] = empty
            
            try:
                item['latitude'] = sel.xpath("@locationx").extract()[0]
            except:
                item['latitude'] = empty
            try:
                item['longitude'] = sel.xpath("@locationy").extract()[0]
            except:
                item['longitude'] = empty
            try:
                price = sel.xpath('div/div/span[@class="badge price"]/text()').extract()[0].split('/')

                item['price'] = price[0].strip(' ').encode('utf-8').strip('€')
                item['period'] = price[1]
                item['currency'] = "€"
            except:
                item['price'] = empty
                item['period'] = empty
                item['currency'] = empty
            
            yield item

