from tastypie import fields
from tastypie.resources import ALL
from tastypie.resources import ModelResource
from travel.models import Event
from travel.models import Trip

class TripResource(ModelResource):
    class Meta:
        queryset = Trip.objects.all()
        resource_name = 'trip'
        filtering = {
            'owner': ALL,
        }

class EventResource(ModelResource):
    trip = fields.ToOneField(TripResource, 'trip')

    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'
        filtering = {
            'trip': ALL,
        }