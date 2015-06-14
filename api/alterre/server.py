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
		self.render("index.html")

class AdsHandler(tornado.web.RequestHandler):
	def get(self):
		db = None
		rows = None
		db    = torndb.Connection(host="localhost", database="test", user="root", password="lifemaker1989")
		rows = None
		ads = dict()
		token = self.get_argument('token', None)
		
		if token != get_guid('alterre'):
			raise tornado.web.HTTPError(401, "You must pass a client api token")
		category = self.get_argument('category', None)
		zone = self.get_argument('zone', None)
		latitude =self.get_argument('lat', None)
		longitude = self.get_argument('lon', None)
		
		radius = self.get_argument('radius', 1)
		print "radius %s " %radius
		rows  = db.query("""select location, latitude, longitude, subcategory, category, price, title, description, url, media from ads""")

		if category is not None:
			_category = db.get("select id, backend_name, name from category where id=%s",(category))["backend_name"]
			print type(category)
			if int(category) < 8:
				rows  = db.query("""select location, latitude, longitude, subcategory, category, price, title, description, url, media from ads where category=%s""",(_category))
			else:
				rows  = db.query("""select location, latitude, longitude, subcategory, category, price, title, description, url, media from ads where subcategory=%s""",(_category))
		if latitude is not None and longitude is not None:
			results = []
			correct_rows = filter(lambda x:valid_float(x["latitude"]) == True, rows)
			center = (float(latitude), float(longitude))
			
			for row in correct_rows:
				target = (float(row["latitude"]), float(row["longitude"]))
				if haversine(center, target) <= float(radius):
					print haversine(center, target), radius
					results.append(row)
					print len(results)
			
			rows = results
			
		if zone is not None:
			rows  = db.query("""
								select location, latitude, longitude, subcategory, category, price, title, description, url, media from ads where location like concat(%s, '%%')
							""", (zone))
					
			total = db.get("""select count(guid) from ads where location like concat(%s, '%%')
							""", (zone))
			ads["ads"] = rows
			ads["zone"] = zone
		
		db.close()
		ads["ads"] = rows
		ads["count"] = len(rows)
		self.set_header("Content-Type", "application/json")
	
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

settings = {

    "template_path": os.path.join(os.path.dirname(__file__), "frontend"),

    "static_path": os.path.join(os.path.dirname(__file__), "static"),

    "debug" : True

}

application = tornado.web.Application([
	(r"/api", MainHandler),
	(r"/api/ads", AdsHandler),
	(r"/ads/categories/housing", HousingAdsHandler),
	(r"/ads/categories/moving", MovingAdsHandler),
	(r"/ads/categories/daily", DailyAdsHandler),
	(r"/ads/categories/meet", MeetAdsHandler),
	(r"/ads/cities/(.*)", CityAdsHandler),
	(r"/api/stats", StatsHandler),
], **settings)

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()