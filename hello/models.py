from django.db import models


# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(null=True,max_length=128)
    email = models.CharField(null=True,max_length=128)
    college = models.CharField(null=True,max_length=128)
    def __str__(self):
        return self.email
