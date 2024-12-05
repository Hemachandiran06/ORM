from django.db import models
from django.contrib import admin
class Bankloan(models.Model):
  date_of_birth=models.DateField(default=0)
  fathers_name=models.CharField(max_length=70,default=0)
  age=models.IntegerField(default=0)
  customerid=models.IntegerField(primary_key="customerid",default=0) 
  accountdetails=models.CharField(max_length=70,default=0)


class BankloanAdmin(admin.ModelAdmin):
 list_display=('date_of_birth','fathers_name','age','customerid','accountdetails')