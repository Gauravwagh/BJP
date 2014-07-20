from django.db import models
from django.contrib.auth.models import User


class FacebookUser(models.Model):
    person = models.ForeignKey(User, null = True, blank = True)
    user_id = models.BigIntegerField(unique = True)
    name = models.CharField(max_length = 200)
    username = models.CharField(max_length = 70, blank = True, unique = True, null=True)
    first_name = models.CharField(max_length = 50, blank = True)
    middle_name = models.CharField(max_length = 50, blank = True)
    last_name = models.CharField(max_length = 50, blank = True)
    GENDER_CHOICES = ( 
            (u'M', u'Male'), 
            (u'F', u'Female'), 
        ) 
    gender = models.CharField(max_length=2, choices = GENDER_CHOICES, blank = True, null = True)
    link = models.URLField(null=True, blank = True)
    verified = models.NullBooleanField(default = False)
    birthday = models.DateField(null = True)
    email = models.EmailField(unique = True, blank= True)
    location = models.CharField(max_length = 50, null = True , blank = True)
    datetime = models.DateTimeField(auto_now_add = True)
    access_token = models.CharField(max_length = 300)    
    ipaddress = models.CharField(max_length = 200,blank = True, null = True)
    country = models.CharField(max_length = 200,blank = True, null = True)
    city = models.CharField(max_length = 200,blank = True, null = True)
    region = models.CharField(max_length = 200,blank = True, null = True)
    
    def __unicode__(self):
        return self.name
