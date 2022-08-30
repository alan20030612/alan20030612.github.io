from django.db import models

# Create your models here.
class web_scraping(models.Model):
    header =  models.CharField(max_length=100)
    arthor = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    url = models.CharField(max_length=500)