from django.db import models

# Create your models here.
class Ureg(models.Model):
    name=models.CharField(max_length=100)
    uname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phno=models.CharField(max_length=100)
    pswd=models.CharField(max_length=100)
    cpswd=models.CharField(max_length=100)
    class Meta:
        db_table="signup"
