#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import France

class EzilizeSpider(scrapy.Spider):
    name = "ezilize"
    categories = {"bricolage":{"category": "daily", "subcategory":"brico"}, 
                  "evenements":{"category":"meet", "subcategory":"events"}, 
                  "mode-vetements":{"category":"daily", "subcategory":"dressing"}, 
                  "sports-loisirs":{"category":"leisure", "subcategory":"sport"},
                   "vehicules":{"category":"moving", "subcategory":"car"}}
    allowed_domains = ["https://ezilize.fr"]
    
    France = France()
    cities = France.cities
    start_urls_0 = list(map(lambda x: "https://ezilize.fr/location/"+str(x), categories))
    
    start_urls = [url+"?p="+str(x) for url in start_urls_0 for x in range(10)]
    
    
    def parse(self, response):
        for sel in response.xpath('//div[@itemtype]'):
            item = AdItem()
            empty = ""
            item['source'] = self.name
            category = response.url.split('?')[0].split('/')[-1]

            item['category'] = self.categories[category]["category"]
            item['subcategory'] = self.categories[category]["subcategory"]

            try:
                item['title'] = sel.xpath('div/div[@class="nsadtitle"]/text()').extract()[0]
            except:
                item['title'] = empty
            try:
                item['media'] = "https:"+sel.xpath('div/div/img/@src').extract()[0]

            except:
                item['media'] = empty
            try:
                item['url'] = self.allowed_domains[0] + sel.xpath('div[@class="nsadprice"]/div/a/@href').extract()[0]
            except:
                item['url'] = empty
            try:
                item['description'] = sel.xpath('div/div[@class="nsadsub"]/text()').extract()[0]

            except:
                item['description'] = empty
            try:
                item['location'] = sel.xpath('div[2]/div[3]/span[2]/text()').extract()[0]
            except:
                item['location'] = empty
            
            item['latitude'] = empty
            item['longitude'] = empty
            try:
                item['price'] = sel.xpath('div[@class="nsadprice"]/div[@class="nsofferamount"]/text()').extract()[0].encode('utf-8').strip('€')
                item['currency'] = "€"
            except:
                item['price'] = empty
                item['currency'] = empty
            item['period'] = "jour"
                
            yield item

