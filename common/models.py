from django.db import models
from uuid import uuid4 as uuid_generator

#
# class MuscleGroupMixin(models.Model):
#     """
#     such as arms, legs, back etc.
#     """
#     group_name = models.CharField(max_length=20)
#
#     class Meta:
#         abstract = True
#
#     def __str__(self):
#         return self.group_name


class UUIDMixin(models.Model):
    """
    Add to have globally unique identifier fields added to a model
    """
    class Meta:
        abstract = True

    uuid = models.UUIDField(unique=True, default=uuid_generator)
