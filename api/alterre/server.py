import os
import tornado.ioloop
import tornado.web
import torndb
import json
import ast
from hashlib import md5
from datetime import datetime
import xml.etree.ElementTree as ET

def get_guid(item):
    """Generates an unique identifier for a given item."""
    # hash based solely in the description field
    return md5(item).hexdigest()

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Here we are integrating the widget.")

class AdsHandler(tornado.web.RequestHandler):
	def get(self):
		db = None
		rows = None
		db    = torndb.Connection(host="localhost", database="test", user="root", password="lifemaker1989")
		rows = None
		ads = dict()
		zone = self.get_argument('zone', None)
		format = self.get_argument('format', None)
		print zone, format
		if zone is not None:
			rows  = db.query("""
								select guid, location, latitude, longitude, subcategory, category, price, title, description, url, media from ads where location like concat(%s, '%%')
							""", (zone))
					
			total = db.get("""select count(guid) from ads where location like concat(%s, '%%')
							""", (zone))
			ads["total"] = total["count(guid)"]	
			ads["zone"] = zone
		else:
			rows  = db.query("""
								select * from ads limit 1000;
							""")
			total = db.get("select count(guid) from ads")
			ads["total"] = total["count(guid)"]	
			
			ads["zone"] = "France"
		 
		db.close()
		self.set_header("Content-Type", "application/xml")
		if format == 'xml':
			data = ET.Element('data')
			for row in rows:
				guid = row["guid"]
				_location = row["location"]
				_lat = row["latitude"]
				_lng = row["longitude"]
				_subcategory = row["subcategory"]
				_category = row["category"]
				_price = row["price"]
				_title = row["title"]
				_description = row["description"]
				_url = row["url"]
				_media = row["media"]

				ad = ET.SubElement(data, 'ad')
				ad.attrib = {"id": guid}
				location = ET.SubElement(ad, 'location')
				print(_location)
				location.attrib = {"city": _location}

				subcategory = ET.SubElement(ad, 'subcategory')
				subcategory.text = _subcategory
				category = ET.SubElement(ad, 'category')
				category.text = _category
				
				price = ET.SubElement(ad, 'price')
				price.text = _price

				title = ET.SubElement(ad, 'title')
				title.text = _title
				description = ET.SubElement(ad, 'description')
				description.text = _description

				url = ET.SubElement(ad, 'url')
				url.text = _url
				
				media = ET.SubElement(ad, 'media')
				media.text = _media
				
			result = str(ET.tostring(data))	
			print result
			self.write(result)
		else:	
			
			ads["ads"] = rows
			self.write(json.dumps(ads))

class HousingAdsHandler(tornado.web.RequestHandler):
	def get(self):
		db = None
		rows = None
		db    = torndb.Connection(host="localhost", database="test", user="root", password="lifemaker1989")
		category = "housing"
		rows  = db.query("""
							select title, description, media, url, price, location from ads where category=%s
						""" ,(category))
		db.close()
		results = dict()
		results["ads"] = rows
		results["total"] = len(rows)
		self.set_header("Content-Type", "application/json")
		self.write(json.dumps(results))

class MovingAdsHandler(tornado.web.RequestHandler):
	def get(self):
		db = None
		rows = None
		db    = torndb.Connection(host="localhost", database="test", user="root", password="lifemaker1989")
		category = "moving"
		rows  = db.query("""
							select title, description, media, url, price, location from ads where category=%s
						""" ,(category))
		db.close()
		results = dict()
		results["ads"] = rows
		results["total"] = len(rows)
		self.set_header("Content-Type", "application/json")
		self.write(json.dumps(results))

class DailyAdsHandler(tornado.web.RequestHandler):
	def get(self):
		db = None
		rows = None
		if MYSQL_DB_HOST == 'localhost':

			db    = torndb.Connection(host="localhost", database="test", user="root", password="lifemaker1989")
		else:
			db    = torndb.Connection(host=MYSQL_DB_HOST, database='alterre', user="adminMwpyBUr", password="XTsiuyKrETU9")

		category = "daily"
		rows  = db.query("""
							select title, description, media, url, price, location from ads where category=%s
						""" , (category))
		db.close()

		results = dict()
		results["ads"] = rows
		results["total"] = len(rows)
		self.set_header("Content-Type", "application/json")
		self.write(json.dumps(results))

class MeetAdsHandler(tornado.web.RequestHandler):
	def get(self):
		db = None
		rows = None
		db    = torndb.Connection(host="localhost", database="test", user="root", password="lifemaker1989")

		category = "meet"
		rows  = db.query("""
							select title, description, media, url, price, location from ads where category=%s
						""", (category))
		db.close()
		results = dict()
		results["ads"] = rows
		results["total"] = len(rows)
		self.set_header("Content-Type", "application/json")
		self.write(json.dumps(results))

class CityAdsHandler(tornado.web.RequestHandler):
	def get(self, city):
		print(city)
		db = None
		rows = None
		db    = torndb.Connection(host="localhost", database="test", user="root", password="lifemaker1989")

		scity = city
		rows  = db.query("""
							select title, description, media, url, price, location from ads where location like concat(%s, '%%')
						""", (scity))
		db.close()

		results = dict()
		results["ads"] = rows
		results["total"] = len(rows)
		self.set_header("Content-Type", "application/json")
		self.write(json.dumps(results))

class StatsHandler(tornado.web.RequestHandler):
	def get(self):
		db = None
		rows = None
		db    = torndb.Connection(host="localhost", database="test", user="root", password="lifemaker1989")
		rows = []
		final = dict()
		zone = self.get_argument('zone', None)

		if zone is not None:
			rows  = db.query("""
								select category, count(guid) from ads where location like concat(%s, '%%') group by category
							""", (zone))
			
			final["zone"] = zone
		else:
			rows  = db.query("""
								select category, count(guid) from ads group by category;
							""")
			final["zone"] = "France"
		db.close()
		

		results = []
		count = 0
		for row in rows:
			result = {}
			result["category"] = row["category"]
			result["total_by_category"] = row["count(guid)"]
			count = count + result["total_by_category"]
			results.append(result)
		final["stats"] = results
		final["total"] = count

		self.set_header("Content-Type", "application/json")
		self.write(json.dumps(final))

application = tornado.web.Application([
	(r"/", MainHandler),
	(r"/api/ads", AdsHandler),
	(r"/ads/categories/housing", HousingAdsHandler),
	(r"/ads/categories/moving", MovingAdsHandler),
	(r"/ads/categories/daily", DailyAdsHandler),
	(r"/ads/categories/meet", MeetAdsHandler),
	(r"/ads/cities/(.*)", CityAdsHandler),
	(r"/api/stats", StatsHandler),
])

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()