from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from workouts.serializers import WorkoutSerializer
from .models import Workout, MuscleGroup


# Create your views here.
@api_view(['GET'])
def get_arms(request):
    arms = Workout.object.get()
    serializer = WorkoutSerializer(arms, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)




# def weekly_workout(request):
#     weekly = WeeklyWorkout.objects.all()
#     serializer = WeeklySerializer(weekly, many=True)
#     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # try:
    #     date = WeeklyWorkout.objects.all()
    # except WeeklyWorkout.DoesNotExist:
    #     raise Http404("Date does not exist")
    # return Response('polls/detail.html', {'poll': p})