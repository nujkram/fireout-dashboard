"""
Django settings for fireout project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from firebasedata import LiveData
from pyrebase import pyrebase
from split_settings.tools import include

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z-3i1^rothz+@hlgaozroj$kbgh2%)1xl$zw#w3e351y3)yw%6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_ID = 1
SITE_URL = 'http://192.168.33.30:8000'

# DEBUGTOOLBAR

DEBUG_TOOLBAR_PANELS = [
  'debug_toolbar.panels.versions.VersionsPanel',
  'debug_toolbar.panels.timer.TimerPanel',
  'debug_toolbar.panels.settings.SettingsPanel',
  'debug_toolbar.panels.headers.HeadersPanel',
  'debug_toolbar.panels.request.RequestPanel',
  'debug_toolbar.panels.sql.SQLPanel',
  'debug_toolbar.panels.staticfiles.StaticFilesPanel',
  'debug_toolbar.panels.templates.TemplatesPanel',
  'debug_toolbar.panels.cache.CachePanel',
  'debug_toolbar.panels.signals.SignalsPanel',
  'debug_toolbar.panels.logging.LoggingPanel',
  'debug_toolbar.panels.redirects.RedirectsPanel',
]

DEBUG_TOOLBAR_CONFIG = {
  'INTERCEPT_REDIRECTS': False,
}

# /DEBUGTOOLBAR

# Application definition

include('../apps.py')

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'corsheaders.middleware.CorsMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.locale.LocaleMiddleware',
  'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'fireout.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
      'templates'
    ],
    'APP_DIRS': True,
    'OPTIONS': {
      'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
      ],
    },
  },
]

WSGI_APPLICATION = 'fireout.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, '../../db.sqlite3'),
  }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Manila'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATICFILES_DIRS = [
  os.path.join(BASE_DIR, "static")
]

STATIC_URL = 'http://192.168.33.30/static/'
STATIC_ROOT = '/var/www/html/static/'

MEDIA_URL = 'http://192.168.33.30/media/'
MEDIA_ROOT = '/var/www/html/media/'

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

REST_FRAMEWORK = {
  'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework.authentication.SessionAuthentication',
  ),
}

# firebase
FIREBASE_CONFIG = {
  'apiKey': 'AIzaSyBcrTQnvu9pwY-o3vQLTnUq42tWQLCOmD4',
  'authDomain': 'https://fireout-7e5dc.firebaseapp.com',
  'databaseURL': 'https://fireout-7e5dc.firebaseio.com',
  'projectId': 'fireout-7e5dc',
  'storageBucket': 'fireout-7e5dc.appspot.com',
  'messagingSenderId': '527618515359',
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'
