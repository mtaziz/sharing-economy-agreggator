#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
import time
from robot.country import all_cities

class DrivySpider(scrapy.Spider):
    name = "lamachineduvoisin"
    category = "daily"
    subcategory = "washing"
    allowed_domains = ["http://www.lamachineduvoisin.fr"]
    # scrap lamachineduvoisin par villes
    cities = all_cities()
    
    start_urls = list(map(lambda x: "http://www.lamachineduvoisin.fr/fr/find/"+str(x), cities))


    def parse(self, response):
        
        for sel in response.xpath('//div[@data-car-id]'):
            item = AdItem()
            empty = ""
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath("div[@class='search_card_content car_content']/a[@class='car_title']/@title").extract()[0]
            except:
                item['title'] = empty
            try:
                item['media'] = sel.xpath('div[@class="search_card_aside car_photo"]/img/@src').extract()[0]
            except:
                item['media'] = empty
            try:
                item['url'] = sel.xpath('div[@class="search_card_content car_content"]/a[@class="car_title"]/@href').extract()[0]
            except:
                item['url'] = empty
            try:
                item['description'] = sel.xpath('div[@class="search_card_content car_content"]/div[@class="car_subtitle"]/text()').extract()[0]
            except:
                item['description'] = empty
            try:
                item['location'] = sel.xpath('div[@class="search_card_content car_content"]/div[@class="car_location"]/text()[2]').extract()[0]
            except:
                item['location'] = empty
            
            item['latitude'] = empty
            item['longitude'] = empty
            
            try:
                item['price'] = sel.xpath('div[@class="search_card_content car_content"]/span[@class="js_car_price car_price"]/strong/text()').extract()[0].encode('utf-8').strip('€')
                item['currency'] = "€"
            except:
                item['price'] = empty
                item['currency'] = empty

            
            try:
                item['period'] = sel.xpath('div[@class="search_card_content car_content"]/span[@class="js_car_price car_price"]/text()').extract()[0]
            except:
                item['period'] = empty

            yield item