from urllib2 import urlopen, Request
from urllib import urlencode
import requests
import sys

API_token = '58242defa30b091a3886b590bd412ea5a7dda3d0'

def getreqauth(reqURL, access_token):
    try:
        response = urlopen(Request(reqURL, headers={'Authorization': 'Token '+ access_token}))
        data = response.read()
    except:
        print sys.exc_info()[1]
        raise
    return data

sampleurl = 'https://formhub.org/api/v1'
param = {}
query = {}
#query[str("name")] = str('Tom') 
query["generalinfo/name"] = "Tom" 
param["query"] = str(query)

dataurl = 'https://formhub.org/api/v1/data/varun4/41082?'
#dataurl_ = 'https://formhub.org/varun4/forms/sample/api?'
dataurl = dataurl+urlencode(param)

print getreqauth(dataurl, API_token)
