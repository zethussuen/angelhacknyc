import datetime
from django.contrib.auth.decorators import login_required
from django.core import serializers
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
    return render_to_response(
            template, locals(), context_instance=RequestContext(request)
        )

@login_required(login_url='/')
def trip(request, trip_id=None, template='main.html'):
    user_profile = request.user.get_profile()
    # import pdb; pdb.set_trace();
    return render_to_response(
        template, locals(), context_instance=RequestContext(request)
    )

def get_trip(request):
    trip_id = request.GET.get('trip', 0)
    start = datetime.datetime.fromtimestamp(float(request.GET.get('start__gte', 0))).strftime("%Y-%m-%d %H:%M")
    end = datetime.datetime.fromtimestamp(float(request.GET.get('end__lte', 0))).strftime("%Y-%m-%d %H:%M")
    data = serializers.serialize("json", Event.objects.filter(trip=trip_id, start__gte=start, end__lte=end))
    return HttpResponse(data)