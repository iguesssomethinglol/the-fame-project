
import requests,datetime,csv,difflib


def installDatabase():
    global mylist
    mylist=[]
    with open("myfile.csv") as fd:
        rd = csv.reader(fd)
        for row in rd:
            for a in row:
                mylist.append(a)      #loads database from csv file



def spellCheck(input):
    a=(difflib.get_close_matches(input,mylist))
    return(a[0])                    #corrects spelling of input (if there's any mistake)



def count(Name):
    dt = datetime.datetime.now()
    month=(dt - datetime.timedelta(31)).strftime('%Y%m%d')+"00"
    today=(dt - datetime.timedelta(1)).strftime('%Y%m%d')+"00"
    if Name not in mylist:
        Name=spellCheck(Name)
    Name=Name.replace(" ","_")
    print(Name)

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



installDatabase()
print(count("Narendra Modi"))
