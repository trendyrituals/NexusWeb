from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.
class ExtendUser(models.Model):
    r = models.OneToOneField(User,on_delete=models.CASCADE)
    added_by = models.CharField(max_length=200)
    def __str__(self):
        return self.r.username