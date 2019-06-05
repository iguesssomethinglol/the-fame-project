#!/usr/bin/env python
# -*- coding: utf-8 -*-

import difflib
import csv
import requests
import datetime





mylist=[]
with open("myfile.csv") as fd:
    rd = csv.reader(fd)
    for row in rd:
        for a in row:
            mylist.append(a)




def is_similar(first, second, ratio):
    return difflib.SequenceMatcher(None, first, second).ratio() > ratio

input = ['Nguyn Minh Trit']

result = [s for f in input for s in mylist if is_similar(f,s, 0.8)]



def dailycount(Name):
    dt = datetime.datetime.now()
    today=(dt - datetime.timedelta(2)).strftime('%Y%m%d')+"00"
    Name=Name.replace(" ","_")

    URL = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{}/daily/{}/{}".format(Name,today,today)
    r = requests.get(url = URL)
    data = r.json()
    return(data['items'][0]['views'])


print(result[0])

"""with open('myfile.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(mylist)"""
