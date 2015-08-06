#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime

class SamboatSpider(scrapy.Spider):
    name = "samboat"
    category = "leisure"
    subcategory = "boat"
    allowed_domains = ["https://www.samboat.fr"]
    # scrap zilok by categories
    start_urls = list(map(lambda x:"https://www.samboat.fr/location-bateau/?&page="+str(x), range(1,31)))


    def parse(self, response):

        for sel in response.xpath('//div[@id="liste_bateaux"]/div'):
            item = AdItem()
            empty = ''
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
            
            try:
                item['description'] = sel.xpath('div[2]/div[@class="row"]/div/div[@class="list-capacite"]/text()').extract()[0].strip('\n')
                
            except:
                item['description'] = empty    
            
            try:
                item['location'] = sel.xpath('div[2]/div[@class="row"]/div/a/span[@class="location"]/text()').extract()[0].strip('\t &nbsp;')
            except:
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
                item['currency'] = '€'
            except:
                item['price'] = empty
                item['currency'] = empty
            
            try:
                item['period'] = sel.xpath('div[2]/div/div[2]/div/span/text()').extract()[0].strip('/ ')
            except:
                item['period']  = empty
	    item['postal_code'] = empty
	    item['evaluations'] = empty
            yield item
