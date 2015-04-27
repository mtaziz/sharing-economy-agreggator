import requests
import ast

def geocode(lat, lng):
	url = "http://nominatim.openstreetmap.org/reverse?"
	payload = {"lat":lat, "lon":lng, "format":"json"}
	r = requests.get(url, params=payload)
	data = ast.literal_eval(r.text)
	location = data["display_name"]
	return location


if __name__ == "__main__":
 lat = 45.03
 lng = 3.508
 location = geocode(lat, lng)
 print location
