import scrapy 
from robot.items import AdItem
import datetime
from geopy.geocoders import Nominatim 

class DrivySpider(scrapy.Spider):
    name = "drivy"
    category = "moving"
    allowed_domains = ["https://www.drivy.com"]
    # scrap zilok by categories
    start_urls = list(map(lambda x: "https://www.drivy.com/search?page="+str(x), range(1,52)))


    def parse(self, response):
        for sel in response.xpath('//div[@data-car-id]'):
            item = AdItem()
            empty = 'unknown'
            try:
                item['source'] = self.name
            except:
                item['source'] = empty
            
            try:
                item['category'] = self.category
            except:
                item['category'] = empty

            try:
                item['title'] = sel.xpath('div[2]/div[2]/a/@title').extract()[0]
            except:
                item['title'] = empty
            try:
                item['media'] = sel.xpath('div[2]/div[1]/img/@src').extract()[0]
            except:
                item['media'] = empty
            try:
                item['url'] = sel.xpath('div[2]/div[2]/a/@href').extract()[0]
            except:
                item['url'] = empty
            try:
                item['description'] = sel.xpath('div[2]/div[2]/div/text()').extract()[0]
            except:
                item['description']= empty
            try:
                item['location'] = sel.xpath('div[2]/div[2]/div[2]/text()[2]').extract()[0]
            except:
                item['location'] = empty
            
            geolocator = Nominatim()
            location = geolocator.geocode(item['location'])
            if item['location'] not empty:
                item['latitude'] = location.latitude or empty
                item['longitude'] = location.longitude or empty
            try:
                item['price'] = sel.xpath('div[3]/text()').extract()[0]
            except:
                item['price'] = empty

            item['price_unit'] = empty
            try:
                item['period'] = sel.xpath('div[3]/span/text()').extract()[0]
            except:
                item['period'] = empty
            yield item