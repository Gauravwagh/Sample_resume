from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import UNUSABLE_PASSWORD
#from PIL import Image
from sorl.thumbnail import ImageField
import string,random,datetime

#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.hashers import PBKDF2PasswordHasher

#from home.forms import RegistrationForm

#import string,random
def get_photo_storage_path(photo_obj, filename):     
        random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(10))
        storage_path = 'img/' + random_string + '_' + filename
        return storage_path
    
class UserProfile(models.Model):
    gender_choice = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.ForeignKey(User, null=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=gender_choice)
    post = models.CharField(max_length=300, null=True, blank=True)
    contact_no = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to=get_photo_storage_path)
    date_of_birth = models.DateField()

    
    
    def __str__(self):
        
        return "%s's profile" % self.user
    
class Pdf_Resume(models.Model):
    myfile = models.FileField(upload_to="get_photo_storage_path")
