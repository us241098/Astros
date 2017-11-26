#!/bin/python3

import json
import turtle
import urllib.request
url='http://api.open-notify.org/astros.json'
response=urllib.request.urlopen(url)
result=json.loads(response.read())
print('People in Space:',result["number"])
people=result['people']
for p in people:
  print(p['name'],'in', p['craft'])

#commit number 2
#test
