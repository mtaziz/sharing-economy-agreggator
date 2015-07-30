#-*- coding:utf-8 -*-
import requests
import json
#Bedycasa API documentation: http://www.bedycasa.com/api/doc/index.html
#generate access_token: valid 3600s

url = "https://www.bedycasa.com/oauth/v2/token"
client_id = "21_48jkpjawhuec0ock0ocgkcco00ocww80c8ookw08wwo0ck0wg8"
client_secret = "40h63xgptxwk4sgsw404g04c0ogoskww4ckoo04ok440c48wg"
grant_type = "client_credentials"
params = {"client_id":client_id, "client_secret":client_secret, "grant_type":grant_type}
req_token = requests.get(url=url, params=params)
result_token = json.loads(req_token.text)
access_token = result_token["access_token"]
print access_token
