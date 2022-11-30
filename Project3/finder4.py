import json
import requests
import pandas as pd


def brewery0(x):
    list1 = ""
    city = x ##"Cincinnati" ##input("What city do you want to search? ")
    num = 5 

    r = requests.get("https://api.openbrewerydb.org/breweries?by_city=%s&per_page=%s" % (city, num))
    data = r.json()

    name = data[0]['name']
    type = data[0]['brewery_type']
    street = data[0]['street']
    list1 = list1 + ('%s, %s, %s'% (name,type,street))

    return list1

def brewery1(x):
    list1 = ""
    city = x ##"Cincinnati" ##input("What city do you want to search? ")
    num = 5 

    r = requests.get("https://api.openbrewerydb.org/breweries?by_city=%s&per_page=%s" % (city, num))
    data = r.json()

    name = data[1]['name']
    type = data[1]['brewery_type']
    street = data[1]['street']
    list1 = list1 + ('%s, %s, %s'% (name,type,street))

    return list1

def brewery2(x):
    list1 = ""
    city = x ##"Cincinnati" ##input("What city do you want to search? ")
    num = 5 

    r = requests.get("https://api.openbrewerydb.org/breweries?by_city=%s&per_page=%s" % (city, num))
    data = r.json()

    name = data[2]['name']
    type = data[2]['brewery_type']
    street = data[2]['street']
    list1 = list1 + ('%s, %s, %s'% (name,type,street))

    return list1

def brewery3(x):
    list1 = ""
    city = x ##"Cincinnati" ##input("What city do you want to search? ")
    num = 5 

    r = requests.get("https://api.openbrewerydb.org/breweries?by_city=%s&per_page=%s" % (city, num))
    data = r.json()

    name = data[3]['name']
    type = data[3]['brewery_type']
    street = data[3]['street']
    list1 = list1 + ('%s, %s, %s'% (name,type,street))

    return list1

def brewery4(x):
    list1 = ""
    city = x ##"Cincinnati" ##input("What city do you want to search? ")
    num = 5 

    r = requests.get("https://api.openbrewerydb.org/breweries?by_city=%s&per_page=%s" % (city, num))
    data = r.json()

    name = data[4]['name']
    type = data[4]['brewery_type']
    street = data[4]['street']
    list1 = list1 + ('%s, %s, %s'% (name,type,street))

    return list1

