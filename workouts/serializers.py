from rest_framework import serializers
from workouts.models import Workout, MuscleGroup, ExerciseSet, ExerciseName
# from django.core import serializers


class GroupSerializer(serializers.Serializer):
    group_name = serializers.CharField()


class ExerciseSerializer(serializers.Serializer):
    exercise_name = serializers.CharField()


class ExerciseSetSerializer(serializers.ModelSerializer):
    exercise = serializers.CharField()
    number_of_sets = serializers.CharField()
    weight = serializers.CharField()
    reps = serializers.CharField()
    notes = serializers.CharField()

    # class Meta:
    #     model = ExerciseName
    #     fields = ('exercise_name',)

    class Meta:
        model = ExerciseSet
        fields = ('exercise', 'number_of_sets', 'weight', 'reps', 'notes',)


class WorkoutSerializer(serializers.ModelSerializer):
    workout_name = serializers.CharField()
    exercise = ExerciseSetSerializer(many=True, read_only=True)

    class Meta:
        model = Workout
        fields = ('workout_name', 'exercise')


class SplitSerializer(serializers.Serializer):
    day = serializers.CharField()
    workouts = serializers.CharField()


class WeeklySerializer(serializers.Serializer):
    week_of = serializers.CharField()


