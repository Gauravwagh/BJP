from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json,urllib,base64,hmac,hashlib

from settings import FB_SECRET_KEY,FB_CANVAS_URL,FB_APP_ID,secure_domain 
from facebook.models import FacebookUser
from facebook.api import create_generic,fql
from login.api import logout_api,create_user,login

# Create your views here.
def base64_url_decode(inp):   
    padding_factor = (4 - len(inp) % 4) % 4
    inp += "="*padding_factor
    return base64.b64decode(unicode(inp).translate(dict(zip(map(ord, u'-_'), u'+/'))))

@csrf_exempt
def fb_app_login(request):             
    try:                
        signed_request = request.POST['signed_request']
        encoded_sig = signed_request.split('.')[0]
        encoded_data = signed_request.split('.')[1]
        sig = base64_url_decode(encoded_sig)
        data = json.loads(base64_url_decode(encoded_data))              
        if (data['algorithm'] !='HMAC-SHA256'):
            raise Http404
        else:
            expected_sig =  hmac.new(FB_SECRET_KEY,encoded_data,digestmod=hashlib.sha256).digest()           
        if sig!=expected_sig:
            raise Http404
        else:                   
            access_token = data['oauth_token']
            query = "SELECT uid, name, username, first_name, middle_name, last_name, sex, birthday, email, current_location FROM user WHERE uid = me()"  
            data = fql(query,access_token)          
            data['fb_api_user_id'] = data['uid']
            data['location'] = data['current_location']
            data['gender'] = data['sex']
            data['id']  = data['uid']
            data['access_token'] = access_token           
            try:                
                fbuser = FacebookUser.objects.get(user_id = data['id'])                          
                if not request.user.is_anonymous():
                    logout_api(request)                  
                login(request,fbuser.person)   
                return HttpResponseRedirect(secure_domain)
            except:                
                data = create_generic(data)                                            
                if data['new_user']:
                    user = create_user(username=data['username'],email=data['email'])                               
                    fbuser = FacebookUser.objects.get(user_id = data['user_id'])
                    fbuser.person = user                    
                    fbuser.save()                   
                    login(request, fbuser.person)                                                                                 
            return HttpResponseRedirect(secure_domain)
    except:
        url =  urllib.urlencode({"redirect_uri":FB_CANVAS_URL})
        url = "https://www.facebook.com/dialog/oauth?client_id="+FB_APP_ID+"&"+url+"&scope=email,offline_access,user_location,publish_stream"
        return render(request,"facebook/redirect.html",{"url":url})