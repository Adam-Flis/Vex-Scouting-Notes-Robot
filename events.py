import json, urllib.request, sys

event = sys.argv[1]
url="https://api.vexdb.io/v1/get_teams?sku="+event
response = urllib.request.urlopen(url)
data = json.loads(response.read())
print(json.dumps(data, sort_keys=True, indent=4))


