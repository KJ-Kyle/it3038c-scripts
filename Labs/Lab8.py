import requests, re
from bs4 import BeautifulSoup

r = requests.get("https://www.mountainproject.com/area/classics/105841134/red-river-gorge").content
soup = BeautifulSoup(r, 'html.parser')
tags = soup.findAll("tr", {"class":re.compile('(route-row)')}) 
for x in tags:
    a = x.findAll("strong")
    b = x.findAll("span", {"class":"rateYDS"})
    print("The route %s has a grade of %s" % (a[0].string,b[0].string))

    
