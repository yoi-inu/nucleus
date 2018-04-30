from django.db import models


class BlogPost(models.Model):

    title = models.CharField(max_length=128)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', related_name='blogposts')
