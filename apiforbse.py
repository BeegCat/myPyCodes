import http.client
import json
conn = http.client.HTTPSConnection("api.bseindia.com")
payload = ''
headers = {
   'User-Agent': 'Apidog/1.0.0 (https://apidog.com)',
   'Accept': '*/*',
   'Host': 'api.bseindia.com',
   'Connection': 'keep-alive',
   'Referer': 'https://api.bseindia.com/BseIndiaAPI/api/SensexGraphData/w?index=98&flag=0&sector=&seriesid=R&frd=null&tod=null'
}
conn.request("GET", "/BseIndiaAPI/api/SensexGraphData/w?index=98&flag=0&sector=&seriesid=R&frd=null&tod=null", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
