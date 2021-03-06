"""
Django settings for technex17 project.

Generated by 'django-admin startproject' using Django 1.9.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import dj_database_url
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=m_wk6=z4z=^4cfv^hkqwb!d3f5i)1rjkih53x(h9t9x6@=@0g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if 'DEBUG' in os.environ:
    if os.environ['DEBUG'] == 'FALSE':
        DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

import django_mobile
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'Auth',
    'ckeditor',
    'authApi',
    'django_mobile',
    'Events',
    'reg',
    'payment',
]
MIDDLEWARE_CLASSES = [
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django_mobile.middleware.MobileDetectionMiddleware',
    'django_mobile.middleware.SetFlavourMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
]


ROOT_URLCONF = 'technex17.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_mobile.context_processors.flavour',
            ],
        },
    },
]

WSGI_APPLICATION = 'technex17.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME':'techteam',
        'USER':'admin',
        'PASSWORD' :'techteam',
        'HOST':'localhost',
        'PORT':'',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


FILE_UPLOAD_HANDLERS = [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
# STATIC_HOST = 'https://d1guaaup0pib3t.cloudfront.net' if not DEBUG else ''
# STATIC_HOST = ''
# STATIC_URL = STATIC_HOST + '/static/'

# if DEBUG:
#     STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#     PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
#     STATICFILES_DIRS = (
#         os.path.join(PROJECT_DIR, 'static').replace('\\','/'),
#     )
# else:
#     STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'
# Extra places for collectstatic to find static files.
'''STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]'''
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)


#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
WHITENOISE_MAX_AGE = 86400

def cache_control(headers, path, url):
    if path.endswith('.css'):
        headers['Cache-Control'] = 'no-cache,must-revalidate; max-age=31536000'
    if path.endswith('.js'):
        headers['Cache-Control'] = 'no-cache,must-revalidate; max-age=31536000'
    if path.endswith('.jpg'):
        headers['Cache-Control'] = 'public; max-age=31536000'
    if path.endswith('.PNG'):
        headers['Cache-Control'] = 'public; max-age=31536000'
    if path.endswith('.png'):
        headers['Cache-Control'] = 'public; max-age=31536000'
    if path.endswith('.svg'):
        headers['Cache-Control'] = 'public; max-age=31536000'

WHITENOISE_ADD_HEADERS_FUNCTION = cache_control

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = (
    'technex.in'
)
#CACHE_CONTROL_MAX_AGE = 604800