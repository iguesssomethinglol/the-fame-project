# -*- coding: utf-8 -*-
import requests
import sys
from bs4 import BeautifulSoup
from lxml import etree
import csv
import json
import urllib3
from urllib import quote


category="List of highest paid American television stars"
pageid='13575907'
mylist=[]

url="https://en.wikipedia.org/w/api.php?action=query&format=json&prop=links&rawcontinue=1&titles="+category+"&pllimit=500"
lm_json=requests.get(url).json()
print(lm_json)


for x in lm_json['query']['pages'][pageid]['links']:
     mylist.append(x['title'].encode('utf-8'))

print(len(mylist))
while(1):
    try:
        newpage=url+"&plcontinue="+lm_json['query-continue']['links']['plcontinue']

        lm_json=requests.get(newpage).json()
        for x in lm_json['query']['pages'][pageid]['links']:
            mylist.append(x['title'].encode('utf-8'))
    except:break

print(len(mylist))




print(len(mylist))

with open("myfile.csv") as fd:
    rd = csv.reader(fd)
    for row in rd:
        for a in row:
            mylist.append(a)
print(len(mylist))




mylist = list(dict.fromkeys(mylist))
print(len(mylist))

with open('myfile.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(mylist)
