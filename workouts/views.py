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