#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime

class MeetupSpider(scrapy.Spider):
    name = "meetup"
    category = "meet"
    subcategory = "events"
    allowed_domains = ["http://www.meetup.com"]
    # scrap by cities
    cities = [
        "Paris","Amiens","Nancy",
        "Rouen","Caen","Evreux","Saint Lo","Rennes","Quimper","Morlaix","Vannes","Strasbourg","Nantes","Clermont Ferrand","Bordeaux","Dax","Chambery",
        "Poitiers","Perpignan","Nimes","Montpellier","Marseille","Nice","Lyon","Toulouse","Limoges","Besancon","Troyes","Orléans","Le mans","Gap","Millau","Brives"
    ]
    #cities = ['paris', 'nantes', 'lille', 'bordeaux', 'nancy', 'nice']
    start_urls_0 = list(map(lambda x: "http://www.meetup.com/cities/fr/"+str(x), cities))
    start_urls = [url+"/?pageToken=default|"+str(x) for url in start_urls_0 for x in [x * 100  for x in range(10)]]
    

    def parse(self, response):
        for sel in response.xpath('//ul[@data-view="card"]/li[@itemtype="http://schema.org/Organization"]'):
            item = AdItem()
            empty = 'unknown'
            item['source'] = self.name
            item['category'] = self.category
            item['subcategory'] = self.subcategory

            try:
                item['title'] = sel.xpath('div/a/text()').extract()[0]
            except: 
                item['title'] = empty

            try:    
                item['media'] = sel.xpath('div/a/img/@src').extract()[0]
            except: 
                item['media'] = empty

            try:
                item['url'] = sel.xpath('div/a/@href').extract()[0]
            except:
                item['url'] = empty
            
            try:        
                item['description'] = sel.xpath('div/a/div[2]/p/text()').extract()[0]
            except:
                item['description'] = empty

            try:
                item['location'] = sel.url.split('/?')[0].split('/')[-1]
            except:
                item['location'] = empty

            
            item['latitude'] = empty
            item['longitude'] = empty

            item['price'] = empty

            item['period'] = empty
            
            yield item
