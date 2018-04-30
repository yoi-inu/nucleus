from django.db import models


class Author(models.Model):

    name = models.CharField(max_length=128)
    avatar_url = models.URLField()
    bio = models.TextField()
