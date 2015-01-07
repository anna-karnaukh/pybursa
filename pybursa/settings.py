"""
Django settings for pybursa project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MEDIA_ROOT = ""
STATIC_ROOT = ""

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_!)1$-uba2!(m(bb7hl08mb(5rvge3l@3pndts68wq*g)!cihc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

from django.utils.translation import ugettext_lazy as _

LANGUAGES = (
    ('ru', _('Russian')),
    ('en', _('English')),
)

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale/'),)
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'students',
    'courses',
    'coaches',
    'debug_toolbar',
    'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pybursa.urls'

WSGI_APPLICATION = 'pybursa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'), )
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(module)s %(levelname)s : %(message)s',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(BASE_DIR,'debug.log'),
        }, 
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'pybursa': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
        'students': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
        'coaches': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
        'courses': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
    },
}
