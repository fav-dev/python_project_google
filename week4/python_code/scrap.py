#!/usr/bin/env python3



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

prefix = "https://content.codecademy.com/courses/beautifulsoup/cacao/"
webpage_response = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
all_tr = soup.find_all("tr")

list_dic_tr = []
for i in all_tr:
    print(i)
    #dic = {}
    #for td in i.findall("td"):
        #dic[class] = class
    #list_dic_tr.append(dic)