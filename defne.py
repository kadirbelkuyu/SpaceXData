import requests
import json


data = requests.get("https://api.spacexdata.com/v2/launches")
content = data.content.decode("utf-8")
data=json.loads(content)
print(data)
print("h")

