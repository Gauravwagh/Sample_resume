from django.conf.urls import patterns, url




urlpatterns = patterns('profiledata.views',
                           (r'^resume/$', 'resume_pdf'),              
                       )