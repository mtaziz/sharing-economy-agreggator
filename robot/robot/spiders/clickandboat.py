#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import France
class ClickandboatSpider(scrapy.Spider):
    name = "clickandboat"
    category = "leisure"
    subcategory = "boat"
    allowed_domains = ["https://www.clickandboat.com"]
    France = France()
    cities = France.cities
    urls = list(map(lambda x:"https://www.clickandboat.com/location-bateau/search?where="+str(x), cities))
    start_urls = [url+"&_page="+str(i) for i in range(30) for url in urls]

    def parse(self, response):

        for sel in response.xpath('//ul[@id="results"]/li'):
            item = AdItem()
            empty = ''
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath('div/div[2]/a/h2[@class="titre-annonce"]/text()').extract()[0]

            except:
                item['title'] = empty
            
            try:
                item['media'] = self.allowed_domains[0] + sel.xpath('div/div/a/img/@src').extract()[0]
            except:
                item['media'] = empty
            
            try:
                item['url'] = self.allowed_domains[0] + sel.xpath('div/div/a/@href').extract()[0]
            except:
                item['url'] = empty
            
            try:
                item['description'] = "capacite "+sel.xpath('div/div[2]/div/div/div[2]/div[2]/p/span/text()').extract()[0]+" personnes" 
                
            except:
                item['description'] = empty    
            
            try:
                item['location'] = sel.xpath('div/div[2]/div/div/div[1]/div[2]/p/span/text()').extract()[0]
            except:
                item['location'] = empty
            item['postal_code'] = 0            
            try:          
                item['latitude'] = sel.xpath('div/input[@class="annonce_lat"]/@value').extract()[0]
            except:
                item['latitude'] = empty

            try:
                item['longitude'] = sel.xpath('div/input[@class="annonce_ltd"]/@value').extract()[0]
            except:
                item['longitude'] = empty
            
            try:
                item['price'] = sel.xpath('div/div[3]/h2/b/span[@class="prix"]/text()').extract()[0]
                item['currency'] = '€'
            except:
                item['price'] = empty
                item['currency'] = empty
            
            try:
                item['period'] = sel.xpath('div/div[3]/h2/small[2]/sup/text()').extract()[0].strip('/')
            except:
                item['period'] = empty

            yield item
