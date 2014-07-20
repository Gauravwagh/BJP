from django import forms
from userview.models import UserViewManifestoIssues,UserViewSuggestion

class UserViewSuggestionForm(forms.ModelForm): # Created a ModelForm class for UserViewSuggestionForm  model that I wish to represent as a form.
    class Meta:   # Provide an association between the ModelForm and a model
        model = UserViewSuggestion # Provide an association between the ModelForm and a model
        exclude = ('user',) #To exclude the user in GUI
    def __init__(self, *args, **kwargs):  
        super(UserViewSuggestionForm,self).__init__(*args, **kwargs)    
        self.fields['issue']  = forms.ModelMultipleChoiceField(queryset=UserViewManifestoIssues.objects.filter(archived=False), widget=forms.CheckboxSelectMultiple(), required=True)
        self.fields['suggestion'].widget.attrs['class']="country"
        self.fields['suggestion_constituency'].widget.attrs['class']="constituency"
        
        
        # Here, we are hiding the foreign key.
               #fields = ('title', 'url', 'views')
               
               #widget=forms.HiddenInput() /// Note that we have set the widget to be hidden with the parameter setting widget=forms.HiddenInput(), 
               #and then set the value to zero with initial=0. This is one way to set the field to zero without giving the control to the user as the 
               #field will be hidden, yet the form will provide the value to the model.