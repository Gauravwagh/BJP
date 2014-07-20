from django.db import models
from django.contrib.auth.models import User
import random,string
# Create your models here.
from location.models import LocationConstituency


def get_photo_storage_path(photo_obj, filename):     
    random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
    storage_path = 'img/' + random_string + '_' + filename
    return storage_path  
    
class UserViewManifestoIssues(models.Model):
    issue = models.TextField()
    user = models.ForeignKey(User)
    image = models.ImageField(null = True, blank = True,upload_to=get_photo_storage_path)    
    archived = models.BooleanField(default=False)   
    datetime= models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.issue  

class UserViewSuggestion(models.Model):    
     
    suggestion = models.TextField("My Suggestions for a Better India",  null = True, blank = True)
    suggestion_constituency = models.TextField("My Suggestions for the betterment of my Constituency", null = True, blank = True)  
    issue = models.ManyToManyField(UserViewManifestoIssues) 
    user = models.ForeignKey(User)
    datetime = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.suggestion  
    