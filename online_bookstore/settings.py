"""
Django settings for online_bookstore project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u)zd-ug74a#cg4#*-j*gvv1qjoh+49uko3il36dj^xm4egjt3x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.gis',
    'tastypie',
    'registration',
    'social.apps.django_app.default',
    'bootstrap3',
    'bootstrap_themes',
    'compressor',
    'store',
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

ROOT_URLCONF = 'online_bookstore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'django.template.context_processors.media',

            ],
        },
    },
]

WSGI_APPLICATION = 'online_bookstore.wsgi.application'


AUTHENTICATION_BACKENDS = (
      'social.backends.facebook.FacebookOAuth2',
	  'django.contrib.auth.backends.ModelBackend' )



# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# in_heroku = False
# if 'DATABASE_URL' in os.environ:
#     in_heroku = True
#
# import dj_database_url
# if in_heroku:
#     DATABASES = {'default': dj_database_url.config()}
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#         }
#     }
#

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
DATABASES = {
    # 'default': {
    #      'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #      'NAME': 'djangoappTest',
    #      'USER': 'postgres',
    #     'PASSWORD': '',
    #     'HOST': 'localhost',
    #     'PORT':'5432'
    # }

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ddkiro43kd0j1d',
        'USER': 'rrukgxvhqtrhgt',
        'PASSWORD': '9eb584565cc1e3cedadd8b11c5b278453d9de4139c27fd06d288e562a60fba7f',
        'HOST': 'ec2-107-22-173-160.compute-1.amazonaws.com',
         # 'HOST': 'localhost',
         'PORT': '5432',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# print STATIC_ROOT
STATIC_URL = '/static/'
COMPRESS_ENABLED = True
STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
		'django.contrib.staticfiles.finders.AppDirectoriesFinder',
		'compressor.finders.CompressorFinder',
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
# print "Static files Dirs", STATICFILES_DIRS
# print "Static Root", STATIC_ROOT
# print "BASE DIR",BASE_DIR
# print "Project dir",PROJECT_ROOT
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

#Registration
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
LOGIN_REDIRECT_URL = '/store/'

# Email Settings

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_HOST_USER = 'postmaster@sandboxbbcb8b207a524e2ba0926d64b529250b.mailgun.org'
EMAIL_HOST_PASSWORD = "7f6aff4aefde37262abded79f1bedf8b"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "bookstore@bookstore-django.herokuapp.com"

# social_auth facebook
SOCIAL_AUTH_FACEBOOK_KEY='1003695826434638'
SOCIAL_AUTH_FACEBOOK_SECRET='59a7c603d6f832b2cabb80eff918c26f'


GEOIP_PATH= 'geo/'

# AUTH_USER_MODEL = 'store.Author'