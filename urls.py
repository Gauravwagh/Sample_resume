from django.conf.urls import patterns, include, url
from django.contrib import admin
import os

import settings

admin.autodiscover()






urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
     #(r'^photologue/', include('photologue.urls')),
)
#Login 
urlpatterns += patterns('profiledata.views',url(r'^$', 'profiles'),)

for app in settings.OUR_APPS:   
    urlpatterns += patterns('',url(r'^'+app+'/', include(app+'.urls',app_name=app)),)
    

if settings.DEBUG:
    urlpatterns += patterns('',
                        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                         {'document_root': settings.MEDIA_ROOT}),
                    )


