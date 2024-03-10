from rest_framework import serializers
from Calendar.models.meeting import Meeting

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = "__all__"