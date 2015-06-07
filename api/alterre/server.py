import os
import tornado.ioloop
import tornado.web
import torndb
import json
import ast
from hashlib import md5
from datetime import datetime

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

		rows  = db.query("select title, description, media, url, price, location from ads")
		db.close()
		self.set_header("Content-Type", "application/json")
		ads = dict()
		ads["ads"] = rows
		ads["total"] = len(rows)
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

application = tornado.web.Application([
	(r"/", MainHandler),
	(r"/ads", AdsHandler),
	(r"/ads/categories/housing", HousingAdsHandler),
	(r"/ads/categories/moving", MovingAdsHandler),
	(r"/ads/categories/daily", DailyAdsHandler),
	(r"/ads/categories/meet", MeetAdsHandler),
	(r"/ads/cities/(.*)", CityAdsHandler),
])

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()