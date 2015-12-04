from rest_framework import serializers
from common.models import MuscleGroupMixin



 class GroupSerializer(serializers.Serializer):
    group_name = serializers.CharField()

