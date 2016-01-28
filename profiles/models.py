from django.db import models
from django.contrib.auth.models import User
from Common.models import UUIDMixin



class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    trainer = models.CharField(max_length=25)

    def __str__(self):
        return
