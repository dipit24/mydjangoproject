from django.db import models
from datetime import datetime

# Create your models here.
class Employee(models.Model):
    f_name=models.CharField(max_length=30)
    l_name=models.CharField(max_length=30)
    age=models.IntegerField()   

class Company(models.Model):
    name=models.CharField(max_length=60)
    c_date=models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return self.name
    
class Language(models.Model):
    name=models.CharField(max_length=30)
    founder=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Employee1(models.Model):
    name=models.CharField(max_length=20, default='Emp Name')
    salary = models.FloatField(default=10000)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    language=models.ManyToManyField(Language)

    def __str__(self):
        return self.name