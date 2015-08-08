#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import France

class BricolibSpider(scrapy.Spider):
    name = "bricolib"
    category = "daily"
    subcategory = "brico"
    allowed_domains = ["http://www.bricolib.net"]
    # scrap zilok by categories
    start_urls = list(map(lambda x: "http://www.bricolib.net/annonces/page/"+str(x), range(1,200)))
    France = France()
    geo = France.geo

    def parse(self, response):
        for sel in response.xpath('//div[@class="post-block"]'):
            item = AdItem()
            empty = ""
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath('div[@class="post-left"]/a/@title').extract()[0]
            except:
                item['title'] = empty
            try:
                item['media'] = "https:"+sel.xpath('div[@class="post-left"]/a/@data-rel').extract()[0]

            except:
                item['media'] = empty
            try:
                item['url'] = sel.xpath('div[@class="post-left"]/a/@href').extract()[0]
            except:
                item['url'] = empty
            try:
                item['description'] = sel.xpath('div[@class="post-right"]/p[@class="post-desc"]/text()').extract()[0]

            except:
                item['description'] = empty
            try:
                item['location'] = sel.xpath('div[@class="post-right"]/p[@class="post-meta"]/span[@class="cp_city"]/text()').extract()[0]
            except:
                item['location'] = empty
            try:
                item['postal_code'] = sel.xpath('div[@class="post-right"]/p[@class="post-meta"]/span[@class="cp_zipcode"]/text()').extract()[0]
            except:         
                item['postal_code'] = 0
            
            try:
                item['latitude'] = float(self.geo[item['location']]['lat'])
            except:
                item['latitude'] = empty

            try:
                item['longitude'] = float(self.geo[item['location']]['lon'])
            except:
                item['longitude'] = empty
            try:
                price = sel.xpath('div[@class="post-right"]/div[@class="price-wrap"]/p[@class="post-price"]/text()').extract()[0].split('/')

                item['price'] = price[0].strip(' ').encode('utf-8').strip('€')
                item['period'] = price[1]
                item['currency'] = "€"
            except:
                item['price'] = empty
                item['period'] = empty
                item['currency'] = empty
            
            item['evaluations'] = empty

            yield item

