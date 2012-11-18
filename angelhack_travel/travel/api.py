import datetime
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
            'start': ['gte'],
            'end': ['lte'],
        }
    def alter_list_data_to_serialize(self, request, data):
        data = data['objects']
        
        for i in range(len(data)):
            if data[i].data['end'] == 0:
                data[i].data['end'] = data[0].data['start']
            data[i].data['start'] = datetime.datetime.fromtimestamp(int(data[i].data['start'])).strftime("%Y-%m-%d %H:%M")
            data[i].data['end'] = datetime.datetime.fromtimestamp(int(data[i].data['end'])).strftime("%Y-%m-%d %H:%M")
            data[i].data['id'] = int(data[i].data['id'])
            data[i].data['allDay'] = False
        return data
        
    '''
    def dehydrate(self, bundle):
        bundle.data['start'] = datetime.datetime.fromtimestamp(int(bundle.data['start'])).strftime("%Y-%m-%d %H:%M")
        bundle.data['end'] = datetime.datetime.fromtimestamp(int(bundle.data['start'])).strftime("%Y-%m-%d %H:%M")
        return bundle
        # import pdb; pdb.set_trace()

    # TODO: Fix implementation of filters, figure out a way to turn timestamp
    # into a nice string
    def build_filters(self, filters):
        import pdb; pdb.set_trace()
        filters['start__gte'] = datetime.datetime.fromtimestamp(int(filters['start__gte'])).strftime("%Y-%m-%d %H:%M")
        filters['end__lte'] = datetime.datetime.fromtimestamp(int(filters['end__lte'])).strftime("%Y-%m-%d %H:%M")
        del filters['_']
        del filters['format']
        return filters
'''