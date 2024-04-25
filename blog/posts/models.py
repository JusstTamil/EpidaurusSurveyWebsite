from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=1000)
    body = models.CharField(max_length=1000000)
    image = models.CharField(max_length=100000)
    author = models.CharField(max_length= 500)
    created_at = models.DateTimeField(default = datetime.now, blank = True)