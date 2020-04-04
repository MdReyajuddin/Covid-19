from django.db import models

# Create your models here.
class Covid(models.Model):
    states=  models.CharField(max_length=100, null=True, blank=True)
    affected =  models.IntegerField(null=True)
    cured =  models.IntegerField(null=True)
    death =  models.IntegerField(null=True)
