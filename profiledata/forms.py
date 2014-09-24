from django import forms
from profiledata.models import UserProfile
#from django.contrib.auth.forms import UserCreationForm

class UserProfileForm(forms.ModelForm):
    class Meta:
        #model= profile
        model = UserProfile
        
        exclude=['user']
        
