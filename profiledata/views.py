from django.shortcuts import render,HttpResponse
from django.shortcuts import render_to_response
from django.db.models import Q
from django.contrib import messages
from django.template import RequestContext

from profiledata.models import UserProfile, Pdf_Resume
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User

def profiles(request):
    return render(request,'profiledata/resume.html',)


 