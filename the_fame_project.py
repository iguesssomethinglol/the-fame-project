
import requests,datetime,csv,difflib


global mylist
mylist=[]
with open("myfile.csv") as fd:
    rd = csv.reader(fd)
    for row in rd:
        for a in row:
            mylist.append(a)


def spellCheck(input):
    def is_similar(first, second, ratio):
        return difflib.SequenceMatcher(None, first, second).ratio() > ratio


    result = [s for f in input for s in mylist if is_similar(f,s, 0.7)]
    try:
        return(result[0])
    except:
        return(input[0])  #corrects spelling from database, returns input if it's unable if similar name doesn't exist in database

def count(Name):
    dt = datetime.datetime.now()
    month=(dt - datetime.timedelta(31)).strftime('%Y%m%d')+"00"
    today=(dt - datetime.timedelta(1)).strftime('%Y%m%d')+"00"
    Name=Name.replace(" ","_")

    URL = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{}/daily/{}/{}".format(Name,month,today)
    r = requests.get(url = URL)
    data = r.json()
    def views(data,duration=""):
        sum=0
        if(duration is "monthly"):
            for x in data['items']:
                sum+=x['views']
            return(sum)

        elif(duration is "daily"):
            return(data['items'][-1]['views'])

        elif(duration is "weekly"):
            for x in data['items'][-7:]:
                sum+=x['views']
            return(sum)
    return([views(data, "daily"),views(data, "weekly"),views(data, "monthly")]) #Returns an array of no. of pageviews[daily,weekly,monthly]




print(count('Wrable'))
