from django.db import models

class LocationCountry(models.Model):
    official_name = models.CharField(max_length = 100)
    def __unicode__(self):
        return self.official_name
    
class LocationState(models.Model):
    country = models.ForeignKey(LocationCountry)
    official_name = models.CharField(max_length = 100)
    def __unicode__(self):
        return self.official_name
    
class LocationConstituency(models.Model):
    state = models.ForeignKey(LocationState)
    official_name = models.CharField(max_length = 100)
    def __unicode__(self):
        return self.official_name
    

