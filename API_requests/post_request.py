import requests
import json
import jsonpath

url="http://localhost:8000/api/maincategory"
file=open("../TestData\\createmaincategory.json",'r')
json_input=file.read()
request_json=json.loads(json_input)

print(request_json)
headers={"Authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7Il9pZCI6IjY1MTVjYWQxYTcxNzNjODAyZWVlN2FiOSIsIm5hbWUiOiJtYXN0ZXIxIiwidXNlcm5hbWUiOiJtYXN0ZXIxIiwiZW1haWwiOiJtYXN0ZXIxQGdtYWlsLmNvbSIsInBob25lIjoiOTI4MzQwOTMyMiIsInBhc3N3b3JkIjoiJDJiJDEyJGp6TGRHV2twaHUyLjA3aWJ5RzJ0OWVZbmw4VEMzVUxsYk9na3pRUmtvcFhCSW9wbjN0QmZHIiwicm9sZSI6ImFkbWluIiwiX192IjowfSwiaWF0IjoxNjk1OTI3MDEyfQ.ys6fDbxc9F-joJivvemJa-GhI83ppRWQ6-33RF8AuTc"}


response=requests.post(url,json=request_json,headers=headers)
print(response.status_code)
print(response.content)