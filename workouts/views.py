from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from workouts.serializers import WorkoutSerializer
from .models import Workout


# Create your views here.
@api_view(['GET'])
def get_arms(request):
    arms = Workout.objects.all()
    serializer = WorkoutSerializer(arms, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)