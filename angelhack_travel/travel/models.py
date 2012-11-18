from django.db import models

# The Event class will store all the time blocks and POIs that show up on the
# calendar for each trip. Users can optionally add an address which will be
# geocoded using the Singly or Zypr APIs.
class Event(models.Model):
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200, blank=True)
  geo_lat = models.CharField(max_length=200, blank=True)
  geo_lon = models.CharField(max_length=200, blank=True)
  url = models.URLField(blank=True)
  notes = models.TextField()
  start = models.DateTimeField()
  end = models.DateTimeField(blank=True)
  trip = models.ForeignKey('Trip')

  # TODO: Implement geocoding on pre-save hook.
  def geocode(self):
    pass

  def __unicode__(self):
    return self.title

# The Trip class will store several Events beloning to a user into a single trip
class Trip(models.Model):
  owner = models.CharField(max_length=200) # TODO: FK to point to User object
  title = models.CharField(max_length=200)

  def __unicode__(self):
    return self.title