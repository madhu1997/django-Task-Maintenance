# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from _warnings import default_action

# Create your models here.

class Trainee(models.Model):  
    user = models.OneToOneField(User,on_delete=models.CASCADE)  
    Full_Name = models.CharField(max_length=100)
    Age = models.IntegerField()  
    Qualification = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username
          
    class Meta:  
        db_table = "traineedetails"
class sessionDetails(models.Model):
    tid = models.ForeignKey(User,default = 1)
    Date = models.DateField()
    session1 = models.CharField(max_length=200)
    session2 = models.CharField(max_length=200)
    session3 = models.CharField(max_length=200)
    session4 = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    
    class Meta:
        db_table = "sessiondetails"
class evaluation(models.Model):
    Eid = models.ForeignKey(User,default = 1)
    NamingConvertion = models.IntegerField()
    validationUse = models.IntegerField()
    exceptionUse = models.IntegerField()
    functionalityUse=models.IntegerField()
    InternetUsage =  models.IntegerField()
    UIdesign =  models.IntegerField()
    AdditionalTask =  models.IntegerField()
    communication =  models.IntegerField()
    logicalSkill =  models.IntegerField()
    debug =  models.IntegerField()
    coding =  models.IntegerField()
    TaskCompletion=models.IntegerField()
    
    class Meta:
        db_table = "evaluation"