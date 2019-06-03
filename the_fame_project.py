
import requests
import datetime


def dailycount(Name):
    dt = datetime.datetime.now()
    today=(dt - datetime.timedelta(1)).strftime('%Y%m%d')+"00"
    Name=Name.replace(" ","_")

    URL = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{}/daily/{}/{}".format(Name,today,today)
    r = requests.get(url = URL)
    data = r.json()
    return(data['items'][0]['views'])


print(dailycount("Narendra Modi"))
