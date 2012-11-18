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
        print result['resourceSets'][0]['resources'][0]['confidence']
        if result['resourceSets'][0]['resources'][0]['confidence'] in ('High', 'Medium'):
            return result['resourceSets'][0]['resources'][0]['point']['coordinates']
    except:
        pass
    
    return None