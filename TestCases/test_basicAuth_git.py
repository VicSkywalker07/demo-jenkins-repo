import requests
from requests.auth import HTTPBasicAuth

def test_with_authentication():
    response= requests.get("https://api.github.com/user",auth=HTTPBasicAuth('VicSkywalker07','LearnDsa@123'))
    print(response.text)
    print(response.status_code)