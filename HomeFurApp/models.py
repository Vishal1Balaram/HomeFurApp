from django.db import models

# Create your models here.

class CustomerAuth(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class AdminProducts(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    condition = models.CharField(max_length=100)
    noofdays = models.IntegerField()
    category = models.CharField(max_length=200)
    options = models.JSONField(max_length=6000)
    rentaloptions = models.JSONField(max_length=6000)
        


def __str__(self):
    return self.first_name + ' ' + self.last_name    