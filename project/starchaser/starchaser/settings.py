"""
Django settings for starchaser project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import yaml
import logging

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# get passwords
passwords_path = os.path.join(BASE_DIR, "passwords.yml")
passwords = yaml.safe_load(open(passwords_path))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = passwords['django']['secret_key']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = passwords['django']['debug']

#ALLOWED_HOSTS = ['Starchaser-dev.us-east-2.elasticbeanstalk.com']
#ALLOWED_HOSTS = ['Starchaser-dev.us-east-2.elasticbeanstalk.com']
#ALLOWED_HOSTS = [
#    'localhost',
#    '127.0.0.1',
#    'ec2-3-22-167-114.us-east-2.compute.amazonaws.com',
#    ]

ALLOWED_HOSTS = [
    'ec2-3-22-167-114.us-east-2.compute.amazonaws.com',
    'localhost',
    '3.22.167.114',
    '127.0.0.1',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'starchaser',
    'app_gameplay',
    'app_player',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

#ROOT_URLCONF = 'starchaser.urls'
ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'starchaser.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

###### this is the in-the-box database
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

###### this is connection to postgresql database all done on windows-side
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'plasticc',
#        'USER': 'postgres',
#        'PASSWORD': '??????',
#        'HOST': '127.0.0.1',
#        'PORT': '5432',
#    }
#}


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
if 'RDS_DB_NAME' in os.environ:
    print("---here1---")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    print("---here2---")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            #'NAME': 'iotd',
            #'USER': 'postgres',
            #'PASSWORD': '1234rtyd%',
            #'HOST' : 'localhost',
            #'PORT' : '5433',
            #'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'plasticc',
            'USER': passwords['wsl_database']['username'],
            'PASSWORD': passwords['wsl_database']['password'],
            'HOST': passwords['wsl_database']['host'],
            'PORT': passwords['wsl_database']['port'],
        }
    }



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
                'OPTIONS': {
                    'min_length': 3,
                }
    },
    #{
    #    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    #},
    # {
    #    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
        # 'level': 'WARNING',
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com//3.0/howto/static-files/



STATIC_ROOT = os.path.join(BASE_DIR, "..", "www", "static")
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

LOGIN_REDIRECT_URL = "player_home"
LOGIN_URL = "player_login"
LOGOUT_REDIRECT_URL = "star_chaser_welcome"
