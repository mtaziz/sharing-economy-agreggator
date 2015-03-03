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
                item['title'] = sel.xpath('div/h2/a/text()').extract()[0].strip("\n ")

            except:
                item['title'] = empty
            try:
                item['media'] = sel.xpath('a/img/@src').extract()[0]
            except:
                item['media'] = empty
            try:
                item['url'] = sel.xpath('a/@href').extract()[0]
            except:
                item['url'] = empty
            try:
                item['description'] = sel.xpath('div/div[@class="boat-info"]/text()').extract()[0].strip("\n ")

            except:
                item['description'] = empty
            try:
                item['location'] = sel.xpath('div/div/h4/strong/text()').extract()[0]
            except:
                item['location'] = empty
                        
            item['latitude'] = empty
            item['longitude'] = empty
            
            try:
                item['price'] = sel.xpath('div[@class="hosting-meta"]/div/span/strong/text()').extract()[0]
            except:
                item['price'] = empty
            
            try:
                item['period'] = sel.xpath('div[3]/span/text()').extract()[0]
            except:
                item['period'] = empty

            yield item