from django.db import models


class MuscleGroupMixin(models.Model):
    """
    such as arms, legs, back etc.
    """
    group_name = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.group_name
