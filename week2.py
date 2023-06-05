#!/usr/bin/env python3 

import os
import requests

path = "/"
dir_list = os.listdir(path)

for file in dir_list:
  dic = {}
  with open(file) as f:
    dic[title] = f.readline()
    dic[name] = f.readline()
    dic[date] = f.readline()
    dic[feedback] = f.read()
  r = requests.post('http://35.188.37.57/feedback/', json=dic)
  print(r.status_code)
