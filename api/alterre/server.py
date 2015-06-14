import os
import tornado.ioloop
import tornado.web
import torndb
import json
import ast
from hashlib import md5
from datetime import datetime
import xml.etree.ElementTree as ET
from haversine import haversine
import re

def get_guid(item):
    """Generates an unique identifier for a given item."""
    # hash based solely in the description field
    return md5(item).hexdigest()

def valid_float(element):
	if element is None:
		return False
	if re.match("^\d+?\.\d+?$", element) is None:
		return False
	return True
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
		latitude =self.get_argument('lat', None)
		longitude = self.get_argument('lon', None)
		radius = self.get_argument('radius', None)
		print radius
		self.set_header("Content-Type", "application/json")
	
		if latitude is not None and longitude is not None and radius is not None:
			results = []
			rows  = db.query("""select location, latitude, longitude, subcategory, category, price, title, description, url, media from ads""")
			correct_rows = filter(lambda x:valid_float(x["latitude"]) == True, rows)
			center = (float(latitude), float(longitude))
			
			for row in correct_rows:
				target = (float(row["latitude"]), float(row["longitude"]))
				if haversine(center, target) <= float(radius):
					print haversine(center, target), radius
					results.append(row)
					print len(results)
			
			ads["ads"] = results
			ads["count"] = len(results)

			self.write(json.dumps(ads))
			db.close()
	
		else:
			if zone is not None:
				rows  = db.query("""
									select location, latitude, longitude, subcategory, category, price, title, description, url, media from ads where location like concat(%s, '%%')
								""", (zone))
						
				total = db.get("""select count(guid) from ads where location like concat(%s, '%%')
								""", (zone))
				ads["ads"] = rows
				ads["total"] = total["count(guid)"]	
				ads["zone"] = zone
			else:
				rows  = db.query("""
									select location, latitude, longitude, subcategory, category, price, title, description, url, media  from ads limit 1000;
								""")
				total = db.get("select count(guid) from ads")
				ads["ads"] = rows
				ads["total"] = total["count(guid)"]	
				
				ads["zone"] = "France"
			self.write(json.dumps(ads))
			db.close()
			 
		self.set_header("Content-Type", "application/json")

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