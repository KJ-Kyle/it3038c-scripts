import json
import requests

color = ['blue','green','black']

for x in color:
    r = requests.get("http://localhost:3000/%s" % x)
    data = r.json()
    try:
        name = data[1]['name']
        color2 = data[1]['color']
        print('%s is %s'% (name,color2))
    except:
        pass
    name = data[0]['name']
    color2 = data[0]['color']
    print('%s is %s'% (name,color2))