"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import django
import os
import sys
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
PROJECT_ROOT = os.path.dirname(__file__)


EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "waghgaurav.g@gmail.com"
EMAIL_HOST_PASSWORD = "110881988"
EMAIL_USE_TLS = True
#sys.path.insert(0, os.path.join(PROJECT_ROOT, ''))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'njhv6junjk@45gj=ss#qlxu3^3wgd0^l#%+sm#e*ieof)f#4w+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

MEDIA_ROOT = os.path.join(SITE_ROOT, 'templates/media/') # path To store the media file

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_PROFILE_MODULE = "account.UserProfile"

if DEBUG == True:
    domain_name = "http://127.0.0.1:8000/" 
'''
STATICFILES_DIRS= (
    "D:/mysite/templates/static",
) '''

STATICFILES_FINDERS=(
                     'django.contrib.staticfiles.finders.FileSystemFinder',
                     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
                     )
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
    'registration',
    'south',
    
)

OUR_APPS = (
            'profiledata',
                      
            )

THIRD_PARTY_APPS = ( 
                     
    )

INSTALLED_APPS +=OUR_APPS
INSTALLED_APPS +=THIRD_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.media',
   # 'multiuploader.context_processors.booleans',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
   os.path.join(SITE_ROOT, 'templates/'),
)

WSGI_APPLICATION = 'wsgi.application'
CRISPY_TEMPLATE_PACK = 'bootstrap3'

import socket
host_name = socket.gethostname()
print host_name

 #Database
#https://docs.djangoproject.com/en/1.6/ref/settings/#databases
if host_name=="gaurav-OptiPlex-GX520":   
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME':SITE_ROOT+'\\sqlite.db',
        }
    }
    
elif host_name=="m-PC":   
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME':SITE_ROOT+'\\db.sqlite3',
        }
    }
elif host_name=="dl-PC":   
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME':SITE_ROOT+'\\db.sqlite3',
        }
    }
    
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'resume_gaurav',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'dramira_admin',
            'PASSWORD': 'TaTaByeBye',
            'HOST': 'mysql.everycrave.me',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
        }
    } 

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ADMIN_MEDIA_PREFIX = '/media/admin/'


ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_REDIRECT_URL = '/'

LOGIN_REDIRECT_URL = '/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


FB_APP_ID = "518889444896033"
FB_SECRET_KEY = "d11ae95af9a36d3519c5c95bfe8d5203"
FB_CANVAS_URL = "https://apps.facebook.com/bjppoll"
secure_domain = 'https://apps.everycrave.me/' 
LOGIN_URL = FB_CANVAS_URL
