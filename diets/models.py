from django.db import models


class ClientStat(models.Model):
    """
    name, body fat, weeks out from show, etc
    """
    name = models.CharField(max_length=150)
    body_fat = models.CharField(max_length=40, blank=True)
    weight = models.CharField(max_length=3, blank=True, null=True)
    show = models.CharField(max_length=100, blank=True)
    weeks_out = models.CharField(max_length=3, blank=True, null=True)

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
    food = models.CharField(max_length=25, unique=True)
    food_group = models.ForeignKey(FoodGroup)

    def __str__(self):
        return self.food


class Diet(models.Model):
    """
    diet form
    """
    date = models.DateField(auto_now_add=True)
    stats = models.ForeignKey(ClientStat)

    def __str__(self):
        return '{} - {}'.format(self.date, self.stats)



class Meal(models.Model):
    """
    Meal Number
    """
    meal_number = models.CharField(max_length=50, blank=True)
    # food = models.ManyToManyField(Food, blank=True)
    # serving_size = models.CharField(max_length=10, blank=True)
    diet = models.ForeignKey(Diet)

    def __str__(self):
        return self.meal_number


class MeasureServing(models.Model):
    meal = models.ForeignKey(Meal)
    food = models.ForeignKey(Food, blank=True)
    serving_size = models.CharField(max_length=50, blank=True)
    diet = models.ForeignKey(Diet)

    def __str__(self):
        return self.serving_size








