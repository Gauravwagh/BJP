# Create your views here.
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404 

from userview.forms import UserViewSuggestionForm
from userview.models import UserViewSuggestion
from account.forms import UserProfileForm
from account.models import UserProfile

@login_required()
def home(request):  
    try:
        profile =   UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None
    try:
        userviewanswer = UserViewSuggestion.objects.get(user=request.user)
    except UserViewSuggestion.DoesNotExist:
        userviewanswer = None                
    if (request.method=="POST"):
        if userviewanswer:
            answerform = UserViewSuggestionForm(request.POST,instance = userviewanswer)
        else:
            answerform = UserViewSuggestionForm(request.POST)
        if profile:   
            userform = UserProfileForm(request.POST)
        else:
            userform = UserProfileForm(request.POST,instance = profile)        
        if answerform.is_valid() and userform.is_valid():
            answer = answerform.save(commit=False)
            profile = userform.save(commit=False)
            answer.user = request.user    
            answer.save() 
            profile.user = request.user   
            profile.save()
            answerform.save_m2m()
            messages.success(request, 'Your suggestion has been taken')  
        else:
            messages.error(request, 'Please enter all required fields')                      
    else:      
        if userviewanswer:
            answerform = UserViewSuggestionForm(instance = userviewanswer)
        else:
            answerform = UserViewSuggestionForm()         
        if profile:   
            userform = UserProfileForm(instance = profile)
        else:
            userform = UserProfileForm()                
    return render(request,'userview/home.html',{'answerform':answerform,'userform':userform})