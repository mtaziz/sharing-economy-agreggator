import scrapy 
from robot.items import AdItem
import datetime
from geopy.geocoders import Nominatim 

class SailsharingSpider(scrapy.Spider):
    name = "sailsharing"
    category = "moving"
    allowed_domains = ["http://www.sailsharing.com/fr"]
    # scrap zilok by categories
    start_urls = list(map(lambda x: "http://www.sailsharing.com/fr/location-bateau/search?page="+str(x), range(1,36)))


    def parse(self, response):
        for sel in response.xpath('//div[@class="block"]'):
            item = AdItem()
            try:
                item['source'] = self.name
            except:
                item['source'] = empty
            
            try:
                item['category'] = self.category
            except:
                print("scraping fails")

            try:
                item['title'] = sel.xpath('div/h2/a/text()').extract()[0]
            except:
                print("scraping fails")
            try:
                item['media'] = sel.xpath('div/a/img/@src').extract()[0]
            except:
                print("scraping fails")
            try:
                item['url'] = sel.xpath('a/@href').extract()[0]
            except:
                print("scraping fails")
            try:
                item['description'] = sel.xpath('div/div[@class="boat-info"]/text()').extract()[0].strip("\n ")

            except:
                print("scraping fails")
            try:
                item['location'] = sel.xpath('div/div/h4/strong/text()').extract()[0]
            except:
                print("scraping fails")
            
            try:
                geolocator = Nominatim()
                location = geolocator.geocode(item['location'])
            
                item['latitude'] = location.latitude
                item['longitude'] = location.longitude
            except:
                print("geocoding not working")
            
            try:
                item['price'] = sel.xpath('div[@class="hosting-meta"]/div/span/strong/text()').extract()[0]
            except:
                print("scraping fails")
            
            try:
                item['period'] = sel.xpath('div[3]/span/text()').extract()[0]
            except:
                print("scraping fails")

            yield item