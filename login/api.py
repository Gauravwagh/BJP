from django.contrib import auth
from django.contrib.auth.models import User

def login(request, user):    
    user.backend = 'django.contrib.auth.backends.ModelBackend'    
    auth.login(request,user)

        
def logout_api(request):
    auth.logout(request)
    
def create_user(username, email = None, password = None):   
    try:
        user = User.objects.get(username=username)
    except:       
        user = User(username=username,email=email)       
        user.save()      
    return user
    
    