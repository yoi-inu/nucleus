from __future__ import absolute_import
import os
import django


def setup(test=False):
    """Sets up django environment. This is essential before performing
    any database operation.
    """
    settings_module = "nucleus.test_config" if test else "nucleus.config"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)
    django.setup()
