from django.db import models
from Common.models import UUIDMixin
from django.utils import timezone as time_manager


class Trainer(models.Model):
    trainer = models.CharField(max_length=25)

    def __str__(self):
        return self.trainer
