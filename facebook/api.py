from facebook.models import FacebookUser
from datetime import datetime 
import json,urllib2




def create_generic(response):
    try:
        fb_api_user_obj = FacebookUser.objects.get(user_id = response['id'])  
       
        if fb_api_user_obj.person:
            fb_api_user_obj.access_token = response['access_token'] 
            response = { 'new_user' : 'false','user_id':response['id']}
            fb_api_user_obj.save()
        else:
            if fb_api_user_obj.username:
                username = fb_api_user_obj.username
            else:
                username = response['first_name'] + response['last_name']           
            response = { 'new_user' : True , 
                        'username' : username, 
                        'email' : fb_api_user_obj.email, 
                        'location' : fb_api_user_obj.location,
                        'user_id' : fb_api_user_obj.user_id }
    except: 
             
        user = FacebookUser(user_id = response['id'])   # create a account        
        try:
            user.name = response['name']
        except:
            pass        
        try:
            username = response['username']
            user.username = username
        except:
            try:
                username = response['first_name'] + response['last_name']
            except:
                pass        
        try:
            user.first_name = response['first_name']
        except:
            pass        
        try:
            user.middle_name = response['middle_name']
        except:
            pass        
        try:
            user.last_name = response['last_name']
        except:
            user.link = response['link']        
        try:
            user.verified = response['verified']
        except:
            pass        
        try:
            user.email= response['email']
        except:
            pass        
        try:
            sex = response['gender']
            if sex == 'male':
                user.gender = 'M'
            elif sex == 'female':
                user.gender = 'F'
        except:
            pass                   
        try:
                
            birthday_in_datetime = datetime.strptime(response['birthday'], '%m/%d/%Y')
            birthday_as_string = birthday_in_datetime.strftime('%Y-%m-%d')
            user.birthday = datetime.strptime(birthday_as_string, '%Y-%m-%d').date()
        except:
            pass                                
        try:
            user.location = response['location']
        except:
            pass        
        user.access_token = response['access_token']   
        user.save()
        #registration_form = get_account('form', type="registration", username = username)
        #HTML = render_to_string("fb_api/forms/register.html", {'form': registration_form, 'user_id' : user.user_id}, context_instance = RequestContext(request)) 
       
        response = { 'new_user' : 'true' , 
                    'username' : username, 
                    'email' : response['email'], 
                    'location' : user.location,
                    'user_id' : response['id'] }   
    return  response   
    
    
def fql(query, access_token):
    query = urllib2.quote(query)
    url = 'https://api.facebook.com/method/fql.query?query='+ query +'&access_token=' + access_token + '&format=JSON'
  
    f = urllib2.urlopen(url)
    data = f.read()
    data = json.loads(data)
    if data:
        return (data[0])
    else:
        return None