from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from workouts.serializers import WorkoutSerializer, WeeklySerializer, SplitSerializer
from .models import Workout, MuscleGroup, WeeklyWorkout, Split


# Create your views here.
@api_view(['GET'])
def get_arms(request):
    arms = MuscleGroup.objects.get(group_name='Arms')
    arms_workouts = Workout.objects.filter(group_name=arms)

    serializer = WorkoutSerializer(arms_workouts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_back(request):
    back = MuscleGroup.objects.get(group_name='Back')
    back_workouts = Workout.objects.filter(group_name=back)

    serializer = WorkoutSerializer(back_workouts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_legs(request):
    legs = MuscleGroup.objects.get(group_name='Legs')
    leg_workouts = Workout.objects.filter(group_name=legs)

    serializer = WorkoutSerializer(leg_workouts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_chest(request):
    chest = MuscleGroup.objects.get(group_name='Chest')
    chest_workouts = Workout.objects.filter(group_name=chest)

    serializer = WorkoutSerializer(chest_workouts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_shoulders(request):
    shoulders = MuscleGroup.objects.get(group_name='Shoulders')
    shoulder_workouts = Workout.objects.filter(group_name=shoulders)

    serializer = WorkoutSerializer(shoulder_workouts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def weekly_workout(request):
    # week_of = WeeklyWorkout.objects.all()
    add_split = Split.objects.all()

    serializer = SplitSerializer(add_split, many=True)
    return Response(serializer.data)


#     serializer = WeeklySerializer(weekly, many=True)
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # try:
    #     date = WeeklyWorkout.objects.all()
    # except WeeklyWorkout.DoesNotExist:
    #     raise Http404("Date does not exist")
    # return Response('polls/detail.html', {'poll': p})