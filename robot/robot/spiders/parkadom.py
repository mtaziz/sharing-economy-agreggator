#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from geopy.geocoders import Nominatim 

class DrivySpider(scrapy.Spider):
    name = "parkadom"
    category = "storing"
    subcategory = "parking"
    allowed_domains = ["http://www.parkadom.com"]
    # scrap zilok by categories
    start_urls = list(map(lambda x: "http://www.parkadom.com/location-parking/resultat-de-recherche?page"+str(x), range(1,52)))


    def parse(self, response):
        for sel in response.xpath('//div[@class="box-parking-dispo"]'):
            item = AdItem()
            empty = "unknown"
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath('div/span[@class="title-parking"]/text()').extract()[0]

            except:
                print("scraping fails")
            try:
                item['media'] = sel.xpath('div/div/div[@class="detail-parking-left"]/div/img/@src').extract()[0]
            except:
                print("scraping fails")
            try:
                item['url'] = sel.xpath('div/div/div[@class="detail-parking-right"]/div[2]/a/@href').extract()[0]
            except:
                print("scraping fails")
            try:
                item['description'] = sel.xpath('div/div/div[@class="detail-parking-left"]/div/img/@alt').extract()[0]
            except:
                print("scraping fails")
            try:
                item['location'] = sel.xpath('div/div/div/div/h1/span/text()').extract()[0]
            except:
                print("scraping fails")
            
            item['latitude'] = empty
            item['longitude'] = empty
            
            try:
                item['price'] = sel.xpath('div/div/div[@class="detail-parking-right"]/div/span/span/text()').extract()[0].encode('utf-8').strip('€')
            except:
                print("scraping fails")
            
            try:
                item['period'] = sel.xpath('div/div/div[@class="detail-parking-right"]/div/span/text()').extract()[0].strip('/')
            except:
                print("scraping fails")

            yield item