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

input=['Anton Raphael Meng']
result = [s for f in input for s in mylist if is_similar(f,s, 0.7)]





print(result)

"""with open('myfile.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(mylist)"""
