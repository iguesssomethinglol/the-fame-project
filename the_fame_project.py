import requests,datetime,csv,difflib,matplotlib.pyplot as plt


class Celebrity:
    def __init__(self,data=[],name="",daily=0,weekly=0,monthly=0):
        self.name = name
        self.data = data
        self.daily=daily
        self.weekly=weekly
        self.monthly=monthly


def installDatabase():#loads database from csv file
    global mylist
    mylist=[]
    with open("/Users/ayushsalik/the-fame-project/myfile.csv") as fd:
        rd = csv.reader(fd)
        for row in rd:
            for a in row:
                mylist.append(a)



def spellCheck(input): #corrects spelling of input (if there's any mistake)
    a=(difflib.get_close_matches(input,mylist))
    return(a[0])



def getData(name): #returns a "Celebrity" object containing various important members
    dt = datetime.datetime.now()
    month=(dt - datetime.timedelta(31)).strftime('%Y%m%d')+"00"
    today=(dt - datetime.timedelta(1)).strftime('%Y%m%d')+"00"
    if name not in mylist:
        name=spellCheck(name)
    name=name.replace(" ","_")

    URL = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{}/daily/{}/{}".format(name,month,today)
    r = requests.get(url = URL)
    data = r.json()
    raw=[]
    daily=monthly=weekly=0
    for x in data['items']:
        monthly+=x['views']
        raw.append(x['views'])
    for x in data['items'][-7:]:
        weekly+=x['views']
    daily=data['items'][-1]['views']
    a=Celebrity(raw,name,daily,weekly,monthly)
    return(a)






installDatabase()
a=getData("Donald Trump")
print(a.daily)
