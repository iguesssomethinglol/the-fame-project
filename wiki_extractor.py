
import requests
from django.utils.encoding import smart_str, smart_unicode
import sys
from bs4 import BeautifulSoup
from lxml import etree
import csv


url = "https://en.wikipedia.org/w/api.php?format=json&action=parse&section=1&page=List_of_YouTubers"
lm_json = requests.get(url).json()

"""
a = u'*'
a=smart_str(a)
lm_html= lm_json["parse"]["text"][a]
soup = BeautifulSoup(lm_html, 'lxml') # Parse the HTML as a string

table = soup.findAll('table')[0].tbody
mylist=[]

data = map(lambda x: (x.findAll(text=True)[1],x.findAll(text=True)[5]),table.findAll('tr'))
names=[]
for x in data:
    if(len(x[0].encode('utf-8'))> 3):
        mylist.append(x[0].encode('utf-8'))


"""

mylist=[]
with open("myfile.csv") as fd:
    rd = csv.reader(fd)
    for row in rd:
        for a in row:
            mylist.append(a)

mylist.append("Christina Perri")

mylist.remove("N")

with open('myfile.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(mylist)
