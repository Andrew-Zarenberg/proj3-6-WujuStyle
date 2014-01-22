import urllib2
import json
from pymongo import MongoClient

def getCoordinates(b):
    url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false"%(b.replace(" ","+"))
    
    request = urllib2.Request(url, headers={'User-Agent':"Firefox Browser"})
    result = urllib2.urlopen(url)
    a = {}
    try: 
        g = json.loads(result.read())["results"][0]

        a["borough"] = g["address_components"][3]["long_name"]
        a["neighborhood"] = str(b.split(",")[0])
        a["lat"] = g["geometry"]["location"]["lat"]
        a["long"] = g["geometry"]["location"]["lng"]
    except:
        return -1;

    return a 

def getDirections(e): 
    url = "http://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&sensor=false"%(e.replace(" "," "))
    
    request = urllib2.Request(url, headers = {'User-Agent': "Firefox"})
    result = urllib2.urlopen(url);
    
    r = {}
    try: 
        k = json.loads(result.read())["results"][0]

        r["how_to_get_there"]=k["directions"][3]["routes"]

    except:
        return -1
    
    return r
