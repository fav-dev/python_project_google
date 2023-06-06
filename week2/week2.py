#! /usr/bin/env python3
import os
import requests

path = "/data/feedback"
dir_list = os.listdir(path)

print(dir_list)
for file_name in dir_list:
  file_path = os.path.join(path, file_name)
  dic = {}

  with open(file_path) as f:
    dic['title'] = f.readline()
    dic['name'] = f.readline()
    dic['date'] = f.readline()
    dic['feedback'] = f.read()
  r = requests.post('http://34.170.164.9/feedback/', json=dic)
  print(r.status_code)

