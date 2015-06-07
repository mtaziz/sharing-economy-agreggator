#-*- coding:utf-8 -*-
import requests
import json
from sqlalchemy import *
from hashlib import md5
import torndb
from datetime import datetime

def get_guid(item):
    """Generates an unique identifier for a given item."""
    # hash based solely in the description field
    return md5(item).hexdigest()

def get_results(link, token):
	response = requests.get(url=link, params={"api_key":token})
	results = json.loads(response.text)
	return results["hits"]

def convert_data(data):
	results = []
	for item in data:
		result = {}
		result["source"] = "jestocke"
		result["category"] = "storing"
		result["subcategory"] = "space"
		result["title"] = item["title"]
		result["url"] = item["url"]
		result["description"] = item["comment"]
		result["location"] = item["address"]
		result["latitude"] = item["lat"]
		result["longitude"] = item["lng"]
		result["media"] = item["pictures"][0]
		result["price"] = item["unit_month_price_with_fee"]
		result["currency"] = "€"
		result["period"] = "par mois"
		results.append(result)
	return results

def store_data(item):
	db    = torndb.Connection(host="localhost", database="test", user="root", password="lifemaker1989")
	print item['url']
	guid = get_guid(item["url"])
	now = datetime.utcnow().replace(microsecond=0).isoformat(' ')

	ret = db.query("""SELECT EXISTS(
	    SELECT 1 FROM ads WHERE guid = %s
	)""", (guid, ))
	print len(ret)
	if len(ret) == 0:
		db.query("""
		    UPDATE ads
		    SET category=%s, subcategory=%s, title=%s, description=%s, price=%s, currency=%s, media=%s, period=%s, location=%s, updated=%s
		    WHERE guid=%s
		""", (item['category'], item['subcategory'], item['title'], item['description'], item['price'], item['currency'], item['media'], item['period'], item['location'], now, guid))
	else:
	    db.insert("""
	        INSERT INTO ads (guid, title, description, url, media, location, latitude, longitude, price, currency, period, source, category, subcategory, updated)
	        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
	    """ , (guid, item['title'], item['description'], item['url'], item['media'], item['location'], item['latitude'], item['longitude'], item['price'], item['currency'], item['period'], item['source'], item['category'], item['subcategory'], now))

	db.close()
	
if __name__ == '__main__':
	url = "https://www.jestocke.com/api/stockage.json"
	api_key = "c5c2a77d-92ce-4126-a265-614e8b510d93"
	results = get_results(url, api_key)
	
	last = convert_data(results)
	for item in last:
		store_data(item)
