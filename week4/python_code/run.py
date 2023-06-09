#!/usr/bin/env python3

import os
import requests
import locale

path = "supplier-data/descriptions/"
dir_list = os.listdir(path)

for file in dir_list:
    image_path = os.path.expanduser("~/supplier-data/images/")
    for infile in os.listdir(image_path):
        if os.path.splitext(file)[0] == os.path.splitext(infile)[0]:
            dic = {}
            with open(os.path.join(path, file)) as f:
                dic['name'] = f.readline()
                weight_str = f.readline().strip()
                weight_str = weight_str.replace("lbs", "")
                dic['weight'] = locale.atof(weight_str)
                dic['description'] = f.read()
                outfile = os.path.splitext(infile)[0]
                dic['image_name'] = outfile.strip(".txt") + ".jpeg"
            r = requests.post('http://35.188.37.57/fruits', json=dic)
            print(r.status_code)




