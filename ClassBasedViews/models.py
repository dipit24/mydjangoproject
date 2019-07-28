from django.db import models as m
from datetime import datetime
# Create your models here.

class Blogs(m.Model):
    title=m.CharField(max_length=30)
    desc=m.TextField()
    dateandtime=m.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.title