
import requests
import datetime



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


def count(Name):
    dt = datetime.datetime.now()
    month=(dt - datetime.timedelta(31)).strftime('%Y%m%d')+"00"
    today=(dt - datetime.timedelta(1)).strftime('%Y%m%d')+"00"
    Name=Name.replace(" ","_")

    URL = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{}/daily/{}/{}".format(Name,month,today)
    r = requests.get(url = URL)
    data = r.json()
    return([views(data, "daily"),views(data, "weekly"),views(data, "monthly")]) #Returns an array of pageviews[daily,weekly,monthly]




print(count("Narendra Modi"))
