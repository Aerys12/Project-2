from rest_framework import generics
from rest_framework.exceptions import NotFound
from Calendar.models.meeting import Meeting
from Calendar.models.calendar import Calendar
from ..serializers.meeting_serializer import MeetingSerializer
from ..permissions import IsCalendarOwner

class MeetingsView(generics.ListAPIView):
    serializer_class = MeetingSerializer
    permission_classes = [IsCalendarOwner]
    
    def get_queryset(self):
        calendar_id = self.kwargs['calendar_id']
        # Get the calendar and verify the user is the creator.
        try:
            calendar = Calendar.objects.get(pk=calendar_id, creator=self.request.user)
        except Calendar.DoesNotExist:
            raise NotFound(detail="Calendar not found")
    
        # Return meetings that are associated with this calendar.
        return Meeting.objects.filter(calendar=calendar)

