#-*- coding:utf8 -*-
import scrapy 
from robot.items import AdItem
import datetime

class TroclegumesSpider(scrapy.Spider):
	name = "troclegumes"
	category = "eating"
	subcategory = "meals"
	allowed_domains = ["http://troc-legumes.fr"]

	regions = [
				"/annonces/region/alsace-23.html", "/annonces/region/aquitaine-1.html", "/annonces/region/auvergne-2.html",
				"/annonces/region/basse-normandie-24.html","/annonces/region/bourgogne-3.html","/annonces/region/bretagne-4.html",
				"/annonces/region/centre-5.html","/annonces/region/champagne-ardenne-6.html","/annonces/region/corse-7.html",
				"/annonces/region/dom-tom-8.html","/annonces/region/franche-comte-9.html","/annonces/region/haute-normandie-17.html",
				"/annonces/region/ile-de-france-10.html","/annonces/region/languedoc-roussillon-11.html","/annonces/region/limousin-12.html",
				"/annonces/region/lorraine-13.html","/annonces/region/midi-pyrenees-14.html","/annonces/region/nord-pas-de-calais-15.html",
				"/annonces/region/pays-de-la-loire-18.html","/annonces/region/picardie-19.html","/annonces/region/poitou-charentes-20.html",
				"/annonces/region/provence-alpes-cote-d-azur-21.html","/annonces/region/rhone-alpes-22.html"
			]

	start_urls = list(map(lambda x: "http://troc-legumes.fr"+str(x), regions))
	
	def parse(self, response):
		for sel in response.xpath('//div[@class="annonces"]'):
			item = AdItem()
			empty = ''
			item['source'] = self.name
			item['category'] = self.category
			item['subcategory'] = self.subcategory

			try:
				item['title'] = sel.xpath('div[@class="cadre-in"]/div[@class="coordonnees"]/b/text()').extract()[0]
			except: 
				item['title'] = empty

			try:	
				item['media'] = sel.xpath('img/@src').extract()[0]
			except: 
				item['media'] = empty

			try:
				item['url'] = sel.xpath('div[@class="cadre-in"]/div[@class="coordonnees"]/a/@href').extract()[0]
			except:
				item['url'] = empty
			
			try:		
				item['description'] = sel.xpath('div[@class="cadre-in"]/div[@class="descriptif"]/text()').extract()[0]
			except:
				item['description'] = empty

			try:
				item['location'] = sel.xpath('div[@class="cadre-in"]/div[@class="coordonnees"]/text()[3]').extract()[0].strip('\n \t')
			except:
				item['location'] = empty

			
			item['latitude'] = empty
			item['longitude'] = empty

			try:
				item['price'] = sel.xpath('div[@class="cadre-in"]/div[@class="coordonnees"]/text()[8]').extract()[0].split(':')[-1].strip('\n').encode('utf-8').split('€')[0]
				item['currency'] = "€"
			except:
				item['price'] = empty
				item['currency'] = empty

			item['period'] = empty
			
			yield item
