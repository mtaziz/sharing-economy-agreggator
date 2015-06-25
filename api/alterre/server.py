import os
import tornado.ioloop
import tornado.web
import torndb
import json
import ast
from hashlib import md5
from datetime import datetime, date
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

def convert_rows_xml(rows):
	data = ET.Element('data')
	for row in rows:
		
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
		#ad.attrib = {"id": guid}
		location = ET.SubElement(ad, 'location')
		location.attrib = {"address": _location, "latitude": _lat, "longitude": _lng}

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
		
	result = ET.tostring(data)	
	return result
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
		format = self.get_argument('format', 'json')
		if token != get_guid('alterre'):
			print get_guid('alterre')
			raise tornado.web.HTTPError(401, "You must pass a client api token")
		category = self.get_argument('category', None)
		zone = self.get_argument('zone', None)
		latitude =self.get_argument('lat', None)
		longitude = self.get_argument('lon', None)
		
		radius = self.get_argument('radius', 1)
		print "radius %s " %radius
		
		if category is not None:
			_category = db.get("select id, backend_name, name from category where id=%s",(category))["backend_name"]
			print _category
			if int(category) < 8:
				rows  = db.query("""select location, latitude, longitude, subcategory, category, price, title, description, url, media from ads where category=%s""",(_category))
			else:
				rows  = db.query("""select location, latitude, longitude, subcategory, category, price, title, description, url, media from ads where subcategory=%s""",(_category))
		if latitude is not None and longitude is not None:
			rows  = db.query("""select location, latitude, longitude, subcategory, category, price, title, description, url, media from ads""")

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
			if format == 'xml':
				self.set_header("Content-Type", "text/xml")
				today = date.today().strftime("%y-%m-%d")
				_file = "flux_"+zone+"_"+today+".xml"
				if os.path.exists(_file):
					
					print "file %s exists " %_file
					self.render(_file)
				else:

					q = '%' + zone + '%'
					rows  = db.query("""
								select guid, subcategory, category, price, title, location, latitude, longitude, description, url, media from ads where location like %s
							""", (q))
		
					result = convert_rows_xml(rows)	
				
					with open(_file,'w+') as flux:
						flux.write(result)
			
					self.render(_file)		
			else:
				q = '%' + zone + '%'
				rows  = db.query("""
								select guid, subcategory, category, price, title, location, latitude, longitude, description, url, media from ads where location like %s
							""", (q))
					
				ads["ads"] = rows
				ads["zone"] = zone
		
		db.close()

		if format == 'json':
			ads["ads"] = rows
			ads["count"] = len(rows)
			self.set_header("Content-Type", "application/json")
		
			self.write(json.dumps(ads))
				 
		if format == 'xml':
			self.set_header("Content-Type", "text/xml")
			result = convert_rows_xml(rows)	
		
			with open('flux.xml','w+') as flux:
				flux.write(result)
			
			self.render("flux.xml")
		
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
			q = '%'+ zone + '%'
			rows  = db.query("""
								select name as category, count(guid) from ads inner join category on category.backend_name=ads.category where location like %s group by category
							""", (q))
			
			final["zone"] = zone
		else:
			rows  = db.query("""
								select name as category, count(guid) from ads inner join category on category.backend_name=ads.category group by category;
							""")
			final["zone"] = "France"
		db.close()
		

		results = []
		count = 0
		for row in rows:
			result = {}
			result["categorie"] = row["category"]
			result["total"] = row["count(guid)"]
			count = count + result["total"]
			results.append(result)
		final["stats"] = results
		final["total"] = count

		self.set_header("Content-Type", "application/json")
		self.write(json.dumps(final))

settings = {

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
