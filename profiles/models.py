from django.db import models
from django.contrib.auth.models import User
from Common.models import UUIDMixin


class Trainer(models.Model):
    name = models.CharField(max_length=200, help_text='Full name of trainer')

    def __str__(self):
        return self.name


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer)

    def __str__(self):
        return
