from django.db import models

# Create your models here.

class Calendar(models.Model):
    month=models.CharField(max_length=30)
    Year=models.IntegerField()
    period=models.CharField(max_length=80)
    startdate=models.DateField()
    enddate=models.DateField()

class Window(models.Model):
    current_window=models.ForeignKey(Calendar,on_delete=models.CASCADE)
    current_year=models.IntegerField()