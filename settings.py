# coding: utf-8

import os


BASE_DIR = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

TIME_ZONE = 'Asia/Seoul'

LANGUAGE_CODE = 'ko-KR'

USE_I18N = False

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/meida/'

SECRET_KEY = 'vzc67d_f_926dns7xv_n)$0-((#*m*)&u_29kzrgfuk_zq(!j7'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

MY_APPS = (
    'main',
    'url_manager',
)

INSTALLED_APPS = MY_APPS + (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'
