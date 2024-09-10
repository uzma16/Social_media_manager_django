from django.db import models

class Post(models.Model):
    content = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    # platform = models.CharField(max_length=100)
