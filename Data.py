import requests
import json
import logging


data = requests.get("https://api.spacexdata.com/v2/launches")
data2 = data.content.decode("utf-8")
data_json = json.loads(data2)
