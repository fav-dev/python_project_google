#!/usr/bin/env python3
import requests

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
with open('/home/student-01-a0a7adef2f7c/supplier-data/images/001.jpeg', 'rb') as opened:
    r = requests.post(url, files={'file': opened})
with open('/home/student-01-a0a7adef2f7c/supplier-data/images/002.jpeg', 'rb') as opened:
    r = requests.post(url, files={'file': opened})
with open('/home/student-01-a0a7adef2f7c/supplier-data/images/003.jpeg', 'rb') as opened:
    r = requests.post(url, files={'file': opened})
with open('/home/student-01-a0a7adef2f7c/supplier-data/images/004.jpeg', 'rb') as opened:
    r = requests.post(url, files={'file': opened})
with open('/home/student-01-a0a7adef2f7c/supplier-data/images/005.jpeg', 'rb') as opened:
    r = requests.post(url, files={'file': opened})
with open('/home/student-01-a0a7adef2f7c/supplier-data/images/006.jpeg', 'rb') as opened:
    r = requests.post(url, files={'file': opened})
with open('/home/student-01-a0a7adef2f7c/supplier-data/images/007.jpeg', 'rb') as opened:
    r = requests.post(url, files={'file': opened})
with open('/home/student-01-a0a7adef2f7c/supplier-data/images/008.jpeg', 'rb') as opened:
    r = requests.post(url, files={'file': opened})
with open('/home/student-01-a0a7adef2f7c/supplier-data/images/009.jpeg', 'rb') as opened:
    r = requests.post(url, files={'file': opened})
with open('/home/student-01-a0a7adef2f7c/supplier-data/images/010.jpeg', 'rb') as opened:
    r = requests.post(url, files={'file': opened})


