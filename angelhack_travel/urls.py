from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'travel.views.home', name='home'),
    # url(r'^angelhack_travel/', include('angelhack_travel.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
