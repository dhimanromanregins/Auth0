from django.db import models
from datetime import datetime

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=100000)
    created_at = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.title
