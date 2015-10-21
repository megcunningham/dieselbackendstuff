from rest_framework import serializers
from workouts.models import Workout, MuscleGroup, ExerciseSet
# from django.core import serializers


class GroupSerializer(serializers.Serializer):
    group_name = serializers.CharField()


class ExerciseSerializer(serializers.Serializer):
    exercise_name = serializers.CharField()


class ExerciseSetSerializer(serializers.Serializer):
    number_of_sets = serializers.CharField()
    weight = serializers.CharField()
    reps = serializers.CharField()
    notes = serializers.CharField()


class WorkoutSerializer(serializers.Serializer):
    workout_name = serializers.CharField()
    exercise = serializers.CharField()


class SplitSerializer(serializers.Serializer):
    day = serializers.CharField()
    workouts = serializers.CharField()


class WeeklySerializer(serializers.Serializer):
    week_of = serializers.CharField()


