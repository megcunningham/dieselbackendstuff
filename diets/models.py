from django.db import models


class Stat(models.Model):
    """
    name, body fat, weeks out from show, etc
    """
    name = models.CharField(max_length=150)
    body_fat = models.CharField(max_length=40)
    weight = models.CharField(max_length=3, blank=True, null=True)
    show = models.CharField(max_length=100)
    weeks_out = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return self.name


class Serving(models.Model):
    """
    Example 4oz, 1 cup, 2 tbsp
    """
    serving_size = models.CharField(max_length=50, blank=True)
    measurement = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.id


class Protein(models.Model):
    """
    type of protein
    """
    protein = models.CharField(max_length=100, unique=True)
    serving = models.ForeignKey(Serving, null=True)

    def __str__(self):
        return self.protein


class Carbohydrate(models.Model):
    """
    type of carb
    """
    carbohydrates = models.CharField(max_length=100, unique=True)
    serving = models.ForeignKey(Serving, null=True)

    def __str__(self):
        return self.carbs


class Green(models.Model):
    """
    green vegetables
    """
    greens = models.CharField(max_length=100, unique=True)
    serving = models.ForeignKey(Serving, null=True)

    def __str__(self):
        return self.greens


class Fat(models.Model):
    """
    dressing, pb, avocado, etc
    """
    fats = models.CharField(max_length=100, unique=True)
    serving = models.ForeignKey(Serving, null=True)

    def __str__(self):
        return self.fats


class Food(models.Model):
    """
    all foods
    """
    protein = models.ForeignKey(Protein, blank=True)
    carbohydrates = models.ForeignKey(Carbohydrate, blank=True)
    greens = models.ForeignKey(Green, blank=True)
    fats = models.ForeignKey(Fat, blank=True)


class Meal(models.Model):
    """
    Meal Number
    """
    meal = models.CharField(max_length=50, unique=True)
    food = models.ForeignKey(Food, blank=True)

    def __str__(self):
        return self.meal


class NewDiet(models.Model):
    """
    diet form
    """
    stats = models.ForeignKey(Stat)
    meal_number = models.ForeignKey(Meal)





