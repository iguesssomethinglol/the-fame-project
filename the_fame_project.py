import requests
import datetime
import csv
import difflib
import matplotlib.pyplot as plt
import base64
from io import BytesIO


class Celebrity:
    def __init__(self, name):

        self._data = self.getRawData(name)
        self.daily = self.getDaily()
        self.weekly = self.getWeekly()
        self.monthly = self.getMonthly()
        self.graph = self.getGraphHTML()

    def getRawData(self, name):  # returns a "Celebrity" object containing various important members
        raw = []
        dt = datetime.datetime.now()
        month = (dt - datetime.timedelta(31)).strftime('%Y%m%d') + "00"
        today = (dt - datetime.timedelta(1)).strftime('%Y%m%d') + "00"
        if name not in mylist:
            name = self.spellCheck(name)
        self.name = name
        name = name.replace(" ", "_")
        URL = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{}/daily/{}/{}".format(
            name, month, today)
        r = requests.get(url=URL)
        data = r.json()
        for x in data['items']:
            raw.append(x['views'])

        return(raw)

    def getDaily(self):
        daily = self._data[-1]
        return(daily)

    def getWeekly(self):
        weekly = 0
        for x in self._data[-7:]:
            weekly += x
        return(weekly)

    def getMonthly(self):
        monthly = 0
        for x in self._data:
            monthly += x
        return(monthly)

    def spellCheck(self, input):  # corrects spelling of input (if there's any mistake)
        a = (difflib.get_close_matches(input, mylist))
        return(a[0])

    def getGraphHTML(self):  # returns html code for graph of all data
        fig = plt.figure()
        ax = fig.gca()
        ax.plot(self._data)
        ax.ylabel = "VIEWS"
        tmpfile = BytesIO()
        fig.savefig(tmpfile, format='png')
        encoded = base64.b64encode(tmpfile.getvalue())

        html = '<img src=\'data:image/png;base64,{}\'>'.format(encoded)
        return(html)


class Database:
    def __init__(self, location):
        self.names=self.getDatabase(location)


    def getDatabase(self,location):  # loads database from csv file
        global mylist
        mylist = []
        with open("/Users/ayushsalik/the-fame-project/{}".format(location)) as fd:
            rd = csv.reader(fd)
            for row in rd:
                for a in row:
                    mylist.append(a)

        return(mylist)


database = Database("myfile.csv")
a = Celebrity("Donald Vq27ixInaunWrCgoKtGTJEq1cuVJTp051X3c4HLrxxhuVmZmp4uJizZ8")
print(a.graph)
