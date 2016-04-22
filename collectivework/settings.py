"""
Django settings for collectivework project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
CONF_FILE = '/opt/collectivework.conf'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

from readconf import DBconfig, DjangoSettings, EmailSettings, TwitterConf
# SECURITY WARNING: keep the secret key used in production secret!
DJANGOSETTINGS = DjangoSettings()
SECRET_KEY = DJANGOSETTINGS.getsecretkey()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['lazimlik.org','www.lazimlik.org']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'collectivework',
    'social.apps.django_app.default',
    'postman',
    'notification',
    'mailer',
    'collectivework.templatetags'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)
AUTHENTICATION_BACKENDS = (
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'collectivework.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',

            ],
        },
    },
]

WSGI_APPLICATION = 'collectivework.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DBCONF = DBconfig()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DBCONF.getdatabase(),
        'USER': DBCONF.getdbuser(),
        'PASSWORD': DBCONF.getdbpass(),
        'HOST': DBCONF.getdbhost(),
        'PORT': DBCONF.getdbport()
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static/'),
#)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = 'media/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] [%(clientip)s - %(user)-8s] %(levelname)s [%(name)s:%(lineno)s]  %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR + "/logfile",
            'maxBytes': 2097152,
            'backupCount': 200,
            'formatter': 'standard',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'WARN',
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'collectivework': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
        },
    }
}
emailconf = EmailSettings()
EMAIL_FROM_ADDRESS = emailconf.fromaddress
EMAIL_USE_TLS = False
EMAIL_HOST = emailconf.host
EMAIL_PORT = emailconf.port
EMAIL_HOST_USER = emailconf.username
EMAIL_HOST_PASSWORD = emailconf.password

# Twitter settings:
tconf = TwitterConf()
SOCIAL_AUTH_TWITTER_KEY = tconf.getcustomerkey()
SOCIAL_AUTH_TWITTER_SECRET = tconf.getcustomersecret()
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True

# Postman Settings
POSTMAN_DISALLOW_ANONYMOUS = True
POSTMAN_DISALLOW_MULTIRECIPIENTS = True
POSTMAN_DISALLOW_COPIES_ON_REPLY = True
POSTMAN_AUTO_MODERATE_AS = True
