from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from models import Event
from models import Trip

import simplejson

def home(request, template='index.html'):
    services = [
        'Facebook',
        'foursquare',
        'Instagram',
        'Tumblr',
        'Twitter',
        'LinkedIn',
        'FitBit',
        'Email'
    ]

    if request.user.is_authenticated():
        user_profile = request.user.get_profile()
        template='main.html'

    response = render_to_response(
            template, locals(), context_instance=RequestContext(request)
        )
    return response