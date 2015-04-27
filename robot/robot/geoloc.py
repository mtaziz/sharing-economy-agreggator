import requests
import ast

def geocode(lat, lng):
	url = "http://nominatim.openstreetmap.org/reverse?"
	payload = {"lat":lat, "lon":lng, "format":"json"}
	r = requests.get(url, params=payload)
	data = ast.literal_eval(r.text)
	location = data["display_name"]
	return location

def geolocate(location):
	url = "http://nominatim.openstreetmap.org/search/%s"%location
	payload = {"format":"json", "limit":1}
	r = requests.get(url, params=payload)
	data = ast.literal_eval(r.text)[0]
	result = {}
	result["lat"] = data["lat"]
	result["lng"] = data["lon"]
	return result

if __name__ == "__main__":
 lat = 45.03
 lng = 3.508
 location = geocode(lat, lng)
 #print location
 result = geolocate("rouen")
 print result
 print geocode(result["lat"], result["lng"])