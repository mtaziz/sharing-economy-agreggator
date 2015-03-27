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
		db    = torndb.Connection(host="localhost", database="test", user="root", password="lifemaker1989")

		rows  = db.query("select title, description, media, url, price, location from ads")
		db.close()

		self.set_header("Content-Type", "application/json")
		self.write(json.dumps(rows))

class HousingAdsHandler(tornado.web.RequestHandler):
	def get(self):
		db    = torndb.Connection(host="localhost", database="test", user="root", password="lifemaker1989")
		category = "housing"
		rows  = db.query("""
							select title, description, media, url, price, location from ads where category=%s
						""" ,(category))
		db.close()

		self.set_header("Content-Type", "application/json")
		self.write(json.dumps(rows))

class MovingAdsHandler(tornado.web.RequestHandler):
	def get(self):
		db    = torndb.Connection(host="localhost", database="test", user="root", password="lifemaker1989")
		category = "moving"
		rows  = db.query("""
							select title, description, media, url, price, location from ads where category=%s
						""" ,(category))
		db.close()

		self.set_header("Content-Type", "application/json")
		self.write(json.dumps(rows))

class DailyAdsHandler(tornado.web.RequestHandler):
	def get(self):
		db    = torndb.Connection(host="localhost", database="test", user="root", password="lifemaker1989")
		category = "daily"
		rows  = db.query("""
							select title, description, media, url, price, location from ads where category=%s
						""" , (category))
		db.close()

		self.set_header("Content-Type", "application/json")
		self.write(json.dumps(rows))
class MeetAdsHandler(tornado.web.RequestHandler):
	def get(self):
		db    = torndb.Connection(host="localhost", database="test", user="root", password="lifemaker1989")
		category = "meet"
		rows  = db.query("""
							select title, description, media, url, price, location from ads where category=%s
						""", (category))
		db.close()

		self.set_header("Content-Type", "application/json")
		self.write(json.dumps(rows))


application = tornado.web.Application([
	(r"/", MainHandler),
	(r"/ads", AdsHandler),
	(r"/ads/housing", HousingAdsHandler),
	(r"/ads/moving", MovingAdsHandler),
	(r"/ads/daily", DailyAdsHandler),
	(r"/ads/meet", MeetAdsHandler),
])

if __name__ == "__main__":
	application.listen(5000)
	tornado.ioloop.IOLoop.instance().start()