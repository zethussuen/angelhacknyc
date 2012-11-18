from django.http import HttpResponse
from models import Event
from models import Trip

# Main application page
def home(request):
  return HttpResponse('Hello world!')

# Returns all trips in json format
def trips(request):
  pass

# Returns all events associated with a trip in json format
def events(request, trip_id=None):
  pass