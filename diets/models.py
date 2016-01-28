from django.db import models
from django.utils import timezone as time_manager


class Date(models.Model):
    date = models.DateField(default=time_manager.now, help_text='Created on')

    def __str__(self):
        return self.date


class ClientStat(Date):
    """
    name, body fat, weeks out from show, etc
    """

    name = models.CharField(max_length=150)
    body_fat = models.CharField(max_length=40, null=True, blank=True)
    weight = models.CharField(max_length=10, blank=True, null=True)
    show = models.CharField(max_length=100, null=True, blank=True)
    weeks_out = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        abstract = False

    def __str__(self):
        return self.name


class FoodGroup(models.Model):
    food_group = models.CharField(max_length=25)

    def __str__(self):
        return self.food_group


class Food(models.Model):
    """
    all foods
    """
    food = models.CharField(max_length=25, unique=True, null=True, blank=True)
    food_group = models.ForeignKey(FoodGroup)

    def __str__(self):
        return self.food


class Diet(ClientStat):
    """
    diet form
    """
    notes = models.TextField(help_text='Trainer notes')

    def __str__(self):
        return '{}'.format(self.date)


class Quantity(models.Model):
    quantity = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.quantity


class MeasureServing(models.Model):
    serving_size = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.serving_size


class Meal(models.Model):
    """
    Meal Number
    """
    note = models.CharField(max_length=50, blank=True, help_text='Meal No.')
    food = models.ForeignKey(Food, null=True, blank=True)
    quantity = models.ForeignKey(Quantity, null=True, blank=True)
    serving_size = models.ForeignKey(MeasureServing, null=True)

    diet = models.ForeignKey(Diet)

    def __str__(self):
        return '{} {} {}'.format(self.food, self.quantity, self.serving_size)


# class MealNumber(Meal):
#     meal_number = models.CharField(max_length=15)
#     diet = models.ForeignKey(Diet)
#
#     def __str__(self):
#         return self.meal_number








