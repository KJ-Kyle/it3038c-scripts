import json
import requests

print('Please enter your zip code:')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=5a1a8d925b0ee952d5259d0f50efa6d5' % zip)
data=r.json()
print(data)
print(data['weather'][0]['description'])