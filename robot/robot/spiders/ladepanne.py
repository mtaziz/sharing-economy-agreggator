#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import France

class LadepanneSpider(scrapy.Spider):
    name = "ladepanne"
    category = "daily"
    subcategory = "brico"
    allowed_domains = ["http://ladepanne.fr"]
    # scrap zilok by categories
    start_urls0 = list(map(lambda x: "https://www.e-loue.com/location/page/%s/?r=9"%str(x), range(1,20)))
    France = France()
    cities = France.cities
    start_urls= ["http://ladepanne.fr/recherche/agrafage/location/Nice-06100"]

    def parse(self, response):
        for sel in response.xpath('//div[@class="block-result line"]'):
            item = AdItem()
            empty = ""
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath("div[2]/a/p/text()").extract()[0]
            except:
                item['title'] = empty
            try:
                item['media'] = self.allowed_domains[0] + sel.xpath('div/a/@href').extract()[0]

            except:
                item['media'] = empty
            try:
                item['url'] = self.allowed_domains[0] + sel.xpath('div/a/@href').extract()[0]
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
                price = sel.xpath('div[2]/div/p/span/text()').extract()[0]

                item['price'] = price.strip(' ').encode('utf-8').strip('€')
                item['currency'] = "€"
            except:
                item['price'] = empty
                item['period'] = empty
                item['currency'] = empty
            
            yield item

