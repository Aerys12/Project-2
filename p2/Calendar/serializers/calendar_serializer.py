from rest_framework import serializers
from ..models.calendar import Calendar
from ..models.availability import Availability
from .availability_serializer import AvailabilityCreateSerializer, AvailabilityViewSerializer


class CalendarCreateSerializer(serializers.ModelSerializer):
    availability_calendar = AvailabilityCreateSerializer(many=True)

    class Meta:
        model = Calendar
        fields = ["title", "description", "duration",
                  "availability_calendar"]

    def create(self, validated_data):
        availability_data = validated_data.pop("availability_calendar")
        calendar = Calendar.objects.create(**validated_data)
        for availability in availability_data:
            Availability.objects.create(calendar=calendar, **availability)
        return calendar

class CalendarViewSerializer(serializers.ModelSerializer):
    availability_calendar = AvailabilityViewSerializer(many=True)
    class Meta:
        model = Calendar
        fields = ["id", "title", "description", "duration",
                  "availability_calendar", 'creator']
        extra_kwargs = {'id': {'read_only': True}}


class CalendarUpdateSerializer(serializers.ModelSerializer):
    availability_calendar = AvailabilityViewSerializer(many=True)

    class Meta:
        model = Calendar
        fields = ['id', 'title', 'description', 'duration', 'availability_calendar']

    def update(self, instance, validated_data):
        availabilities_data = validated_data.pop('availability_calendar', [])
        instance = super().update(instance, validated_data)

        current_availability_ids = set(instance.availability_calendar.values_list('id', flat=True))
        updated_availability_ids = set()

        for availability_data in availabilities_data:
            availability_id = availability_data.get('id', None)
            #if 'id' in the current database update it:
            if availability_id and Availability.objects.filter(id=availability_id, calendar=instance).exists():
                avail_instance = Availability.objects.get(id=availability_id)
                for key, value in availability_data.items():
                    setattr(avail_instance, key, value)
                avail_instance.save()
                updated_availability_ids.add(availability_id)
            #if id does not exists (we should give new availability id value of or None but it might raise is_valid error -1)
            else:
                new_availability = Availability.objects.create(calendar=instance, **availability_data)
                updated_availability_ids.add(new_availability.id)
        availabilities_to_delete = current_availability_ids - updated_availability_ids
        #after updating any changes remove deleted fields
        if availabilities_to_delete:
            Availability.objects.filter(id__in=availabilities_to_delete).delete()

        return instance



