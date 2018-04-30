"""
Settings to override in testing environment.
"""
from __future__ import unicode_literals
from __future__ import absolute_import
import os

from .config import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'TEST': {
            'NAME': os.path.join(PROJECT_DIR, 'test_nucleus.db')
        }

        # The following are not required for sqlite database. Add it
        # when using postgres, mysql or oracledb.
        # ----------------------------------------------------------
        # 'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
        # 'PORT': os.environ.get('DATABASE_PORT', 1234),
        # 'USER': os.environ.get('DATABASE_USER', 'user123'),
        # 'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'pass123')
    }
}
