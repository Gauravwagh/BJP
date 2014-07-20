from django.db import models
from django.contrib.auth.models import User
import random,string


def get_photo_storage_path(photo_obj, filename):     
    random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
    storage_path = 'img/profile/' + random_string + '_' + filename
    return storage_path  

class UserProfile(models.Model):
    user = models.OneToOneField(User,primary_key=True)   
    image = models.ImageField(upload_to=get_photo_storage_path, null = True, blank=True)
    location = models.ForeignKey('location.LocationConstituency',null = True, blank=True) 
    phone_number = models.CharField( max_length = 10,verbose_name="Mobile Number 10 digits",null = True, blank=True, default=None)
