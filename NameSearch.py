import urllib2
"define my API key"
mykey = "70962437b30570e"  
import requests
import json

api_key = mykey
"define variable url that stores the url for fullcontact API"

url = "https://api.fullcontact.com/v2/person.json"

"creat function serch that takes in twitter names  as argument"

def serch(**kwargs):
    if 'apiKey' not in kwargs:
        kwargs['apiKey'] = api_key

        " get request to the fullcontact API"
    r = requests.get(url, params=kwargs)

    " loads json data from the fullcontact site and saves it data"
    data= json.loads(r.text)

    "prints the status code"
    print data['status']

    "assigns the the social prifiles part of the data recieved to variable y"
    y=data ['socialProfiles']

    "iterate over the data prining the social profile details of the said individual"
    for i in range(len(y)):
    	print y[i]
    return

"calling the serch function to serch for the social profile of denis"
serch(twitter='denis')


