import requests
import json
import jsonpath

url="http://localhost:8000/api/maincategory/"

response=requests.get(url)

print(response.content)
print(response.headers)
print(response.status_code)
print(response.elapsed)

assert response.status_code==200

json_response=json.loads(response.text)

name=jsonpath.jsonpath(json_response,'data[0].name')
print(name)
