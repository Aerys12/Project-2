from rest_framework import serializers
from Calendar.models.calendar import Calendar

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = "__all__"
        