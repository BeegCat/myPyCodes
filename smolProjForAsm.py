import requests
import json

url= "https://parfumistas.com/wp-json/wp/v2/perfume/2180"

response= requests.get(url)

response_json= response.json()
print(json.dumps(response_json, indent=4))
print(response.status_code)