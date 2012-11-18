from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from travel.api import EventResource
from travel.api import TripResource

admin.autodiscover()

# API Creation
v1_api = Api(api_name="v1")
v1_api.register(EventResource())
v1_api.register(TripResource())

urlpatterns = patterns('',
    url(r'^$', 'travel.views.home', name='home'),
    url(r'^singly/', include('singly.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
