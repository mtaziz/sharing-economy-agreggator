#-*- encoding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime
from robot.country import France
class DrivySpider(scrapy.Spider):
    name = "drivy"
    category = "moving"
    subcategory = "car"
    allowed_domains = ["https://www.drivy.com"]
    # scrap zilok by categories
    France = France()
    geo = France.geo
    urls = []
    for k,v in geo.items():
        url = "https://www.drivy.com/search?latitude="+str(v["lat"])+"&longitude="+str(v["lon"])+"&city_display_name="+k+"&area_type=city"  
        urls.append(url)
    start_urls = [url+"&page="+str(i) for url in urls for i in xrange(1,51)]
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
                item['url'] = self.allowed_domains[0] + sel.xpath('div[@class="search_card_content car_content"]/a[@class="car_title"]/@href').extract()[0]
            except:
                item['url'] = empty
            try:
                item['description'] = sel.xpath('div[@class="search_card_content car_content"]/div[@class="car_subtitle"]/text()').extract()[0]
            except:
                item['description'] = empty
            try:
                item['location'] = sel.xpath('div[@class="search_card_content car_content"]/div[@class="car_location"]/text()[2]').extract()[0].strip('\n')
            except:
                item['location'] = response.url.split('city_display_name=')[1].split('&')[0]
            
            try:
                item['evaluations'] = float(sel.xpath('div[2]/div[3]/div/span/text()').extract()[0])
            except:
                item['evaluations'] = empty
            
            item['postal_code'] = empty
            url_city = response.url.split('city_display_name=')[1].split('&')[0]
            try:
                item['latitude'] = float(self.geo[url_city]['lat'])
            except:
                item['latitude'] = empty

            try:
                item['longitude'] = float(self.geo[url_city]['lon'])
            except:
                item['longitude'] = empty

            try:
                item['price'] = sel.xpath('div[@class="search_card_content car_content"]/span[@class="js_car_price car_price"]/strong/text()').extract()[0].encode('utf-8').strip('€')
                item['currency'] = "€"
            except:
                item['price'] = empty
                item['currency'] = empty
            try:
                item['period'] ="jour" 
            except:
                item['period'] = empty

            yield item


