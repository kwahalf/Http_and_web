import urllib2
mykey = "70962437b30570e"
import requests
import json

api_key = mykey
url = "https://api.fullcontact.com/v2/person.json"

def serch(**kwargs):
    if 'apiKey' not in kwargs:
        kwargs['apiKey'] = api_key
    r = requests.get(url, params=kwargs)
    data= json.loads(r.text)
    print data['status']
    y=data ['socialProfiles']
    for i in range(len(y)):
    	print y[i]
    return
serch(twitter='denis')


