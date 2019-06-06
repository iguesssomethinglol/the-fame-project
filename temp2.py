# -*- coding: utf-8 -*-
import requests
import sys
from bs4 import BeautifulSoup
from lxml import etree
import csv
import json
import urllib3
from urllib import quote


category="American_television_actresses"
mylist=[]

url="https://en.wikipedia.org/w/api.php?action=query&format=json&list=categorymembers&continue=-%7C%7C&cmtitle=Category%3A"+category+"&cmlimit=500"
lm_json=requests.get(url).json()
for x in lm_json['query']['categorymembers']:
     mylist.append(x['title'].encode('utf-8'))
while(1):
    try:
        newpage=url+"&cmcontinue="+lm_json['continue']['cmcontinue']

        lm_json=requests.get(newpage).json()
        for x in lm_json['query']['categorymembers']:
            mylist.append(x['title'].encode('utf-8'))
    except:break



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
