
from pathlib import Path
import os

import os
from pathlib import Path
import environ

env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY","change-this")

DEBUG = True

ALLOWED_HOSTS = ['sruniq.com']

INSTALLED_APPS = [
 'django.contrib.admin',
 'django.contrib.auth',
 'django.contrib.contenttypes',
 'django.contrib.sessions',
 'django.contrib.messages',
 'django.contrib.staticfiles',
 'storages',
 'certificates',
 "corsheaders",
]

MIDDLEWARE = [
 'django.middleware.security.SecurityMiddleware',
 'django.contrib.sessions.middleware.SessionMiddleware',
 "corsheaders.middleware.CorsMiddleware",
 'django.middleware.common.CommonMiddleware',
 'django.middleware.csrf.CsrfViewMiddleware',
 'django.contrib.auth.middleware.AuthenticationMiddleware',
 'django.contrib.messages.middleware.MessageMiddleware',
 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rk_certificate_portal.urls'

TEMPLATES = [{
 'BACKEND':'django.template.backends.django.DjangoTemplates',
 'DIRS':[BASE_DIR/'templates'],
 'APP_DIRS':True,
 'OPTIONS':{'context_processors':[
  'django.template.context_processors.debug',
  'django.template.context_processors.request',
  'django.contrib.auth.context_processors.auth',
  'django.contrib.messages.context_processors.messages',
 ]},
}]

DATABASES = {
 'default': {
  'ENGINE':'django.db.backends.sqlite3',
  'NAME':BASE_DIR/'db.sqlite3'
 }
}

LANGUAGE_CODE='en-us'
TIME_ZONE='UTC'
USE_TZ=True
STATIC_URL='/static/'
STATIC_ROOT=BASE_DIR/'staticfiles'


# settings.py

# ... other settings ...




LOGIN_URL='/login/'
LOGIN_REDIRECT_URL='/dashboard/'

DEFAULT_FILE_STORAGE='storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME=os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_REGION_NAME=os.environ.get("AWS_S3_BUCKET_REGION")
# AWS_DEFAULT_ACL = None
AWS_S3_FILE_OVERWRITE = False
AWS_QUERYSTRING_AUTH = True
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_S3_BUCKET_REGION =os.environ.get("AWS_S3_BUCKET_REGION")
# s3 static settings
#STATIC_LOCATION = 'static'
#STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
#STATICFILES_STORAGE = 'rk_certificate_portal.storage_backend.StaticStorage'
# s3 public media settings
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'

# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
