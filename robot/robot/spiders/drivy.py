#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from geopy.geocoders import Nominatim 

class DrivySpider(scrapy.Spider):
    name = "drivy"
    category = "moving"
    subcategory = "car"
    allowed_domains = ["https://www.drivy.com"]
    # scrap zilok by categories
    start_urls = list(map(lambda x: "https://www.drivy.com/search?page="+str(x), range(1,52)))


    def parse(self, response):
        for sel in response.xpath('//div[@data-car-id]'):
            item = AdItem()
            empty = "unknown"
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath("div[@class='search_card_content car_content']/a[@class='car_title']/@title").extract()[0]
            except:
                print("scraping fails")
            try:
                item['media'] = sel.xpath('div[@class="search_card_aside car_photo"]/img/@src').extract()[0]
            except:
                print("scraping fails")
            try:
                item['url'] = sel.xpath('div[@class="search_card_content car_content"]/a[@class="car_title"]/@href').extract()[0]
            except:
                print("scraping fails")
            try:
                item['description'] = sel.xpath('div[@class="search_card_content car_content"]/div[@class="car_subtitle"]/text()').extract()[0]
            except:
                print("scraping fails")
            try:
                item['location'] = sel.xpath('div[@class="search_card_content car_content"]/div[@class="car_location"]/text()[2]').extract()[0]
            except:
                print("scraping fails")
            
            item['latitude'] = empty
            item['longitude'] = empty
            
            try:
                item['price'] = sel.xpath('div[@class="search_card_content car_content"]/span[@class="js_car_price car_price"]/strong/text()').extract()[0].encode('utf-8').strip('€')
            except:
                print("scraping fails")
            
            try:
                item['period'] = sel.xpath('div[@class="search_card_content car_content"]/span[@class="js_car_price car_price"]/text()').extract()[0]
            except:
                print("scraping fails")

            yield item