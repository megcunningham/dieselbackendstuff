from django.db import models


class MuscleGroup(models.Model):
    """
    such as arms, legs, back etc.
    """
    group_name = models.CharField(max_length=20)

    def __str__(self):
        return self.group_name


class DifficultyLevel(models.Model):
    """
    Workout level of difficulty
    """
    level = models.CharField(max_length=50, unique=True, default='Beginner')

    def __str__(self):
        return self.level


class ExerciseName(models.Model):
    """
    name of a single exercise such as lateral raises
    """
    group_name = models.ForeignKey(MuscleGroup)
    name = models.CharField(max_length=75, unique=True)

    def __str__(self):
        return self.name


# class ExerciseSet(models.Model):
#     """
#      The directions on how the exercise should be executed
#     """
#     exercise = models.ForeignKey(ExerciseName)
#     number_of_sets = models.CharField(max_length=30)
#     weight = models.CharField(max_length=100, blank=True)
#     reps = models.CharField(max_length=100, blank=True)
#     notes = models.TextField(blank=True)
#     group_name = models.ForeignKey(MuscleGroup)
#
#     def __str__(self):
#         return '{}-{} sets for {} reps ({})'.format(self.exercise, self.number_of_sets, self.reps, self.notes)


class CompleteSet(models.Model):
    group_name = models.ForeignKey(MuscleGroup)
    exercise = models.ForeignKey(ExerciseName)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.exercise, self.notes)


class NumberOfSet(models.Model):
    set_number = models.CharField(max_length=30, blank=True, null=True)
    weight = models.CharField(max_length=30, blank=True, null=True)
    reps = models.CharField(max_length=30, blank=True, null=True)
    exercise_set = models.ForeignKey(CompleteSet)

    def __str__(self):
        return self.set_number


class Workout(models.Model):
    """
    The named workout with collection of exercises and directions
    """
    workout_name = models.CharField(max_length=60, unique=True)
    group_name = models.ForeignKey(MuscleGroup)
    level = models.ForeignKey(DifficultyLevel)
    exercise = models.ManyToManyField(CompleteSet)

    def __str__(self):
        return self.workout_name


class WeeklyWorkout(models.Model):
    """
    Raw id field to enter in a date
    """
    week_of = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.week_of)


class Split(models.Model):
    """
    Inline model with WeeklyWorkout, this is a form that splits
    up a given number of workouts for the week
    """
    week_of = models.ForeignKey(WeeklyWorkout)
    days = models.CharField(max_length=2)
    workouts = models.ManyToManyField(Workout)

    def __str__(self):
        return '{}'.format(self.week_of)






