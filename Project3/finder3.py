import json
import requests
import pandas as pd


def brewery(a, c):
    try:
        list1 = "["
        city = a 
        num = c

        r = requests.get("https://api.openbrewerydb.org/breweries?by_city=%s&per_page=%s" % (city, num))
        data = r.json()

        for x in range(num):
            name = data[x]['name']
            type = data[x]['brewery_type']
            street = data[x]['street']
            list1 = list1 + ('"%s - %s - %s",' % (name,type,street))

        list1 = list1[:-1] + "]"
        list2 = eval(list1)
        return list2
    except:
        uhoh = "fail"
        return uhoh

    