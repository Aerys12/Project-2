from rest_framework import serializers
from ..models.availability import Availability


class AvailabilityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ['date_time', 'preference']


class AvailabilityViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ['id', 'date_time', 'preference']
        extra_kwargs = {'id': {'read_only': True}}


class AvailabilityUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Availability
        fields = ['id', 'date_time', 'preference']

