from rest_framework import serializers
from workouts.models import Workout, MuscleGroup, ExerciseSet


class WorkoutSerializer(serializers.Serializer):
    workout_name = serializers.CharField()
    group_name = serializers.CharField()
    exercise = serializers.CharField()
