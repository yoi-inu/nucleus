"""
This configuration file serves the same purpose as the django settings
file when nucleus is used as a standalone package.
"""
from __future__ import unicode_literals
from __future__ import absolute_import
import os


SECRET_KEY = '8s!!+9hojio25-mefs62esm@q0v=+a*1zm9lp#+tjp5lf!8%=!'
PROJECT_DIR = os.path.abspath(
    os.path.dirname(os.path.dirname(__file__))
)

##########################
# Database configuration #
##########################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'nucleus.db'),

        # The following are not required for sqlite database. Add it
        # when using postgres, mysql or oracledb.
        # ----------------------------------------------------------
        # 'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
        # 'PORT': os.environ.get('DATABASE_PORT', 1234),
        # 'USER': os.environ.get('DATABASE_USER', 'user123'),
        # 'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'pass123')
    }
}


##########################
# Django apps to include #
##########################

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'nucleus'
)


#####################
# Timezone settings #
#####################

USE_TZ = True
TIME_ZONE = 'Asia/Kolkata'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# You can add more settings in this file as per your models. For       #
# example, if you models need to access static files, you can define   #
# STATIC_ROOT and STATIC_URL here.                                     #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
