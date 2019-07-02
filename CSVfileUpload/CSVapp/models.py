from datetime import datetime

from django.db import models

# Create your models

class form(models.Model):
    name = models.CharField(max_length=200)
    start_date_time = models.DateTimeField('date published')


class form1(models.Model):
    name1=models.CharField(max_length=200)
    start_date_time1=models.DateTimeField('date published')
    q1=models.ForeignKey(form,on_delete=models.CASCADE)







