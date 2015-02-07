from scrapy import Spider, Item, Field
import pickle

class Post(Item):
	title = Field()

class BlogSpider(Spider):

	name, start_urls = 'blogspider', ['http://fr.zilok.com/location/k-paris']

	def parse(self, response):

		results = [Post(title=e.extract()) for e in response.css("td h4 a::text")]
		with open('zilok_results.txt', 'a') as zilok:
				mypickle=pickle.Pickler(zilok)
				mypickle.dump(results)
