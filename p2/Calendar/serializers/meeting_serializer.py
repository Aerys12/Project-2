from rest_framework import serializers
from Calendar.models.meeting import Meeting

class MeetingSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Meeting model.
    """
    class Meta:
        model = Meeting
        fields = "__all__"
