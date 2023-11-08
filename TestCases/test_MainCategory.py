import requests
import json
import jsonpath
import os
import datetime
import pytest


def test_getMainCategory():
    url="http://localhost:9000/api/maincategory"
    
    # json_response=json.loads(response.text)
    try:
        response=requests.get(url)
        print(response.json()["count"])
    except BaseException:
        print("exception caught")

# @pytest.mark.skip(reason="no way of currently testing this")
def test_createmaincategory():

    # login
    url="http://localhost:9000/api/user/login"
    payload={"username":"master1","password":"Master@123"}
    resp=requests.post(url,json=payload)
    token=(resp.json()["token"])



    url="http://localhost:9000/api/maincategory"
    
    file=open("TestData\createmaincategory.json",'r')
    
    inputfile=file.read()
    payload=json.loads(inputfile)
    payload["name"]=payload["name"]+str(datetime.datetime.now())
    headers={"Authorization":token}


    response=requests.post(url=url,json=payload,headers=headers)
    print(response.text)
    assert response.status_code==201

def test_updatemaincategory():
    url="http://localhost:9000/api/maincategory/6515da1d4ec99d181a0cd694"
    
    file=open("TestData\createmaincategory.json",'r')
    
    inputfile=file.read()
    payload=json.loads(inputfile)
    payload["name"]=payload["name"]+str(datetime.datetime.now())
    headers={"Authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7Il9pZCI6IjY1MTVjYWQxYTcxNzNjODAyZWVlN2FiOSIsIm5hbWUiOiJtYXN0ZXIxIiwidXNlcm5hbWUiOiJtYXN0ZXIxIiwiZW1haWwiOiJtYXN0ZXIxQGdtYWlsLmNvbSIsInBob25lIjoiOTI4MzQwOTMyMiIsInBhc3N3b3JkIjoiJDJiJDEyJGp6TGRHV2twaHUyLjA3aWJ5RzJ0OWVZbmw4VEMzVUxsYk9na3pRUmtvcFhCSW9wbjN0QmZHIiwicm9sZSI6ImFkbWluIiwiX192IjowfSwiaWF0IjoxNjk1OTI3MDEyfQ.ys6fDbxc9F-joJivvemJa-GhI83ppRWQ6-33RF8AuTc"}


    response=requests.put(url=url,json=payload,headers=headers)
    print(response.text)
    assert response.status_code==200
