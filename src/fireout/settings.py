import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from split_settings.tools import include

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get("DEBUG", default=0))

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

SITE_ID = 1
SITE_URL = os.environ.get("SITE_URL")

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

include('apps.py')

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
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
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE"),
        "NAME": os.environ.get("SQL_DATABASE"),
        "USER": os.environ.get("SQL_USER"),
        "PASSWORD": os.environ.get("SQL_PASSWORD"),
        "HOST": os.environ.get("SQL_HOST"),
        "PORT": os.environ.get("SQL_PORT"),
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

STATIC_URL = os.environ.get("STATIC_URL")
STATIC_ROOT = os.environ.get("STATIC_ROOT")

MEDIA_URL = os.environ.get("MEDIA_URL")
MEDIA_ROOT = os.environ.get("MEDIA_ROOT")

# firebase
FIREBASE_CONFIG = {
    'apiKey': os.environ.get("FIREBASE_APIKEY"),
    'authDomain': os.environ.get("FIREBASE_AUTHDOMAIN"),
    'databaseURL': os.environ.get("FIREBASE_DATABASEURL"),
    'projectId': os.environ.get("FIREBASE_PROJECTID"),
    'storageBucket': os.environ.get("FIREBASE_STORAGEBUCKET"),
    # 'messagingSenderId': '',
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'