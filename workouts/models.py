from django.db import models


class MuscleGroup(models.Model):
    """
    such as arms, legs, back etc.
    """
    group_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.group_name


class Exercise(models.Model):
    """
    name of a single exercise
    such as lateral raises
    """
    name = models.CharField(max_length=75, unique=True)
    group_name = models.ForeignKey(MuscleGroup)

    def __str__(self):
        return self.name


class ExerciseSet(models.Model):
    """
     The directions on how the exercise
     should be executed
    """
    exercise = models.ForeignKey(Exercise)
    number_of_sets = models.CharField(max_length=15)
    weight = models.CharField(max_length=200, blank=True)
    reps = models.CharField(max_length=200, blank=True)
    notes = models.CharField(max_length=200, blank=True)
    group_name = models.ForeignKey(MuscleGroup)

    def __str__(self):
        return '{}-{} sets for {} reps ({})'.format(self.exercise, self.number_of_sets, self.reps, self.notes)


class Workout(models.Model):
    """
    The named workout with collection of exercises and directions
    """
    workout_name = models.CharField(max_length=60, unique=True)
    group_name = models.ForeignKey(MuscleGroup)
    exercise = models.ManyToManyField(ExerciseSet)

    def __str__(self):
        return '{} {} {}'.format(self.group_name, self.workout_name, self.exercise)



