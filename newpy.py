import http.client
import json
conn = http.client.HTTPSConnection("api.bseindia.com")
payload = ''
headers = {
   'User-Agent': 'Apidog/1.0.0 (https://apidog.com)',
   'Accept': '*/*',
   'Host': 'api.bseindia.com',
   'Connection': 'keep-alive',
   'Referer': 'https://api.bseindia.com/BseIndiaAPI/api/IndexMovers/w'
}
conn.request("GET", "/BseIndiaAPI/api/IndexMovers/w", payload, headers)
res = conn.getresponse()
data = res.read()
#print(data.decode("utf-8"))
print(data.json())
'''import requests
import json

url= 'https://api.bseindia.com/BseIndiaAPI/api/IndexMovers/w'

response= requests.get(url)

response_json= response.json()
print(json.dumps(response_json, indent=4))
print(response.status_code)'''