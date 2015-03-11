#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime

class SupermarmiteSpider(scrapy.Spider):
    name = "supermarmite"
    category = "eating"
    subcategory = "meals"
    allowed_domains = ["http://www.super-marmite.com"]
    # scrap by cities
    cities = [
        "Paris","Amiens","Nancy",
        "Rouen","Caen","Evreux","Saint Lo","Rennes","Quimper","Morlaix","Vannes","Strasbourg","Nantes","Clermont Ferrand","Bordeaux","Dax","Chambery",
        "Poitiers","Perpignan","Nimes","Montpellier","Marseille","Nice","Lyon","Toulouse","Limoges","Besancon","Troyes","Orléans","Le mans","Gap","Millau","Brives"
    ]
    #cities = ['paris', 'nantes', 'lille', 'bordeaux', 'nancy', 'nice']
    start_urls_0 = list(map(lambda x: "http://www.super-marmite.com/meals?where="+str(x), cities))
    start_urls = [url+"&page="+str(x) for url in start_urls_0 for x in range(10)]
    

    def parse(self, response):
        for sel in response.xpath('//ul[@class="users"]/li'):
            item = AdItem()
            empty = 'unknown'
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath('div/div[@class="content"]/h3[@class="orange"]/a/text()').extract()[0]
            except: 
                item['title'] = empty

            try:    
                item['media'] = sel.xpath('div/a/img/@src').extract()[0]
            except: 
                item['media'] = empty

            try:
                item['url'] = sel.xpath('div/div[@class="content"]/h3[@class="orange"]/a/@href').extract()[0]
            except:
                item['url'] = empty
            
            try:        
                item['description'] = sel.xpath('div/div[@class="content"]/p[@class="description"]/text()').extract()[0]
            except:
                item['description'] = empty

            try:
                item['location'] = sel.xpath('div/div[@class="content"]/div[@class="map_information"]/p/text()[2]').extract()[0]
            except:
                item['location'] = empty

            
            item['latitude'] = empty
            item['longitude'] = empty

            try:
                item['price'] = response.xpath('div/p[@class="price orange"]/text()').extract()[0].split('/')[0].encode('utf-8').strip('€')

            except:
                item['price'] = empty

            try:
                while i > 2 and i < 9:
                    item['period'] = item['period'] + "\n" + response.xpath('div/div[@class="content"]/p[@class="meta"]/text()[%d]' %i).extract()[0]
                    i += 1
            except:
                item['period'] = empty
            
            yield item
