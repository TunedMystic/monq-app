"""
Django settings for webapp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^ujom94*or-!h7!l2e=f)+_$)*0=!wzq@_kb)u_ar90u)v-szu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
if not DEBUG:
  #ALLOWED_HOSTS = [".nitrousbox.com", "127.0.0.1", "0.0.0.0", "localhost"]
  ALLOWED_HOSTS = [".herokuapp.com"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "social.apps.django_app.default",
    "taggit",
    # Site-specific apps.
    "nil",
    "userextension",
    "snippet",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'webapp.urls'

WSGI_APPLICATION = 'webapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = "staticfiles"

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)


# Python Social Auth Settings

LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/login"
SOCIAL_AUTH_LOGIN_REDIRECT_URL = "/"

TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.static',
   'django.core.context_processors.tz',
   'django.contrib.messages.context_processors.messages',
   'social.apps.django_app.context_processors.backends',
   'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_FACEBOOK_KEY = "334742830038719"
SOCIAL_AUTH_FACEBOOK_SECRET = "1a591b1d6034e8d3be479080f27ba5ba"

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "808726665778-pmbtui7cbl54brf30bbun3383e776dmm.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "z_6U7_a8UK57Ou-nw3Y3yzm4"

SOCIAL_AUTH_TWITTER_KEY = "0oiz8mSVpeqQXzFG6PeAZJu1D"
SOCIAL_AUTH_TWITTER_SECRET = "1rBrH6v2mzcdRrDzXhojr4dbKLLKI7yX5qZEtN9zs6bvwsMoDB"


# Django-Debug-Toolbar Settings
DDJT = True
if DEBUG and DDJT:
  INSTALLED_APPS += ("debug_toolbar.apps.DebugToolbarConfig",)
  
  INTERNAL_IPS = ("127.0.0.1", "192.168.241.1", "54.84.169.151", "24.90.8.194")

