from rest_framework import serializers
from Calendar.models.meeting import Meeting


class MeetingSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Meeting model.
    """
    class Meta:
        model = Meeting
        fields = ['title', 'receiver', 'status', 'start_time', 'calendar']
        read_only_fields = ['calendar']

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

