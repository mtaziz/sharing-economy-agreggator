#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime

class SailsharingSpider(scrapy.Spider):
    name = "samboat"
    category = "moving"
    subcategory = "boat"
    allowed_domains = ["https://www.samboat.fr"]
    # scrap zilok by categories
    start_urls = ["https://www.samboat.fr/location-bateau/"]


    def parse(self, response):
        for sel in response.xpath('//div[@id="liste_bateaux"]/div'):
            item = AdItem()
            empty = 'unknown'
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath('div/div/a/img/@alt').extract()[0]

            except:
                item['title'] = empty
            try:
                item['media'] = sel.xpath('div/div/a/img/@src').extract()[0]
            except:
                item['media'] = empty
            try:
                item['url'] = sel.xpath('div/div/a/@href').extract()[0]
            except:
                item['url'] = empty

            item['description'] = empty
            item['location'] = empty
            
            try:          
                item['latitude'] = sel.xpath('div/input[@class="annonce_lat"]/@value').extract()[0]
            except:
                item['latitude'] = empty

            try:
                item['longitude'] = sel.xpath('div/input[@class="annonce_ltd"]/@value').extract()[0]
            except:
                item['longitude'] = empty
            try:
                item['price'] = sel.xpath('div/input[@class="annonce_px_jour"]/@value').extract()[0]
            except:
                item['price'] = empty
            
            try:
                item['period'] = sel.xpath('div[3]/span/text()').extract()[0]
            except:
                item['period'] = empty

            yield item