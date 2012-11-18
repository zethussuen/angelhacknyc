import requests
import settings
import simplejson
import urllib

def geocode(address):
    url = 'http://dev.virtualearth.net/REST/v1/Locations'
    params = {
        'query': address,
        'o': 'json',
        'key': settings.BING_API_KEY
    }
    response = requests.get(url, params=params)
    result = simplejson.loads(response.content)
    
    try:
        if result['resourceSets'][0]['resources'][0]['confidence'] in ('High', 'Medium'):
            return result['resourceSets'][0]['resources'][0]['point']['coordinates']
    except:
        pass
    
    return None

def directions(from_address, to_address):
    url = 'http://dev.virtualearth.net/REST/v1/Routes'
    params = {
        'waypoint.1': from_address,
        'waypoint.2': to_address,
        'maxSolutions': 1,
        'key': settings.BING_API_KEY
    }
    response = requests.get(url, params=params)
    result = simplejson.loads(response.content)
    
    # result['resourceSets'][0]['resources'][0]['travelDuration']
    return result