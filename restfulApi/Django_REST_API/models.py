from django.db import models

# Create your models here.
class Data(models.Model):
    data_name = models.CharField(max_length=100)
    data_year = models.IntegerField()
    data_category = models.CharField(max_length=30)