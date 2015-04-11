import os
import tornado.ioloop
import tornado.web
import torndb
import json
import ast
from hashlib import md5
from datetime import datetime

MYSQL_DB_HOST = os.environ.get('OPENSHIFT_MYSQL_DB_HOST') if os.environ.get('OPENSHIFT_MYSQL_DB_HOST') else 'localhost'

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
		if MYSQL_DB_HOST == 'localhost':
			db    = torndb.Connection(host="localhost", database="test", user="root", password="lifemaker1989")

		else:
			db    = torndb.Connection(host=MYSQL_DB_HOST, database='alterre', user="adminMwpyBUr", password="XTsiuyKrETU9")

		rows  = db.query("select title, description, media, url, price, location from ads")
		db.close()
		self.set_header("Content-Type", "application/json")
		ads = dict()
		ads["ads"] = rows
		self.write(json.dumps(ads))

class HousingAdsHandler(tornado.web.RequestHandler):
	def get(self):
		db = None
		rows = None
		if MYSQL_DB_HOST == 'localhost':

			db    = torndb.Connection(host="localhost", database="test", user="root", password="lifemaker1989")
		else:
			db    = torndb.Connection(host=MYSQL_DB_HOST, database='alterre', user="adminMwpyBUr", password="XTsiuyKrETU9")
		
		category = "housing"
		rows  = db.query("""
							select title, description, media, url, price, location from ads where category=%s
						""" ,(category))
		db.close()

		self.set_header("Content-Type", "application/json")
		self.write(json.dumps(rows))

class MovingAdsHandler(tornado.web.RequestHandler):
	def get(self):
		db = None
		rows = None
		if MYSQL_DB_HOST == 'localhost':

			db    = torndb.Connection(host="localhost", database="test", user="root", password="lifemaker1989")
		else:
			db    = torndb.Connection(host=MYSQL_DB_HOST, database='alterre', user="adminMwpyBUr", password="XTsiuyKrETU9")

		category = "moving"
		rows  = db.query("""
							select title, description, media, url, price, location from ads where category=%s
						""" ,(category))
		db.close()

		self.set_header("Content-Type", "application/json")
		self.write(json.dumps(rows))

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

		self.set_header("Content-Type", "application/json")
		self.write(json.dumps(rows))
class MeetAdsHandler(tornado.web.RequestHandler):
	def get(self):
		db = None
		rows = None
		if MYSQL_DB_HOST == 'localhost':

			db    = torndb.Connection(host="localhost", database="test", user="root", password="lifemaker1989")
		else:
			db    = torndb.Connection(host=MYSQL_DB_HOST, database='alterre', user="adminMwpyBUr", password="XTsiuyKrETU9")

		category = "meet"
		rows  = db.query("""
							select title, description, media, url, price, location from ads where category=%s
						""", (category))
		db.close()

		self.set_header("Content-Type", "application/json")
		self.write(json.dumps(rows))

class CityAdsHandler(tornado.web.RequestHandler):
	def get(self, city):
		print(city)
		db = None
		rows = None
		if MYSQL_DB_HOST == 'localhost':

			db    = torndb.Connection(host="localhost", database="test", user="root", password="lifemaker1989")
		else:
			db    = torndb.Connection(host=MYSQL_DB_HOST, database='alterre', user="adminMwpyBUr", password="XTsiuyKrETU9")

		scity = city
		rows  = db.query("""
							select title, description, media, url, price, location from ads where INSTR(location, %s)
						""", (scity))
		db.close()

		self.set_header("Content-Type", "application/json")
		self.write(json.dumps(rows))
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