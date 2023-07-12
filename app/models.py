from django.db import models

# Create your models here.
class Member(models.Model):
    mid = models.IntegerField()
    mname = models.CharField(max_length=70)
    memail = models.EmailField(max_length=70)
    mnumber = models.BigIntegerField()
    
