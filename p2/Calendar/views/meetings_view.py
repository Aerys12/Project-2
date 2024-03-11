from rest_framework import generics
from rest_framework.exceptions import NotFound
from Calendar.models.meeting import Meeting
from Calendar.models.calendar import Calendar
from ..serializers.meeting_serializer import MeetingSerializer
from ..permissions import IsCalendarOwner

class MeetingsView(generics.ListAPIView):
    """
    A view for retrieving a list of meetings associated with a calendar.

    This view requires the user to be the owner of the calendar.

    Attributes:
        serializer_class (class): The serializer class used for serializing the meeting data.
        permission_classes (list): The list of permission classes required for accessing this view.
    """

    serializer_class = MeetingSerializer
    permission_classes = [IsCalendarOwner]
    
    def get_queryset(self):
        """
        Get the queryset of meetings associated with the calendar.

        Returns:
            queryset: The queryset of meetings associated with the calendar.
        
        Raises:
            NotFound: If the calendar does not exist.
        """
        calendar_id = self.kwargs['calendar_id']
        
        # Get the calendar and verify the user is the creator.
        try:
            calendar = Calendar.objects.get(pk=calendar_id, creator=self.request.user)
        except Calendar.DoesNotExist:
            raise NotFound(detail="Calendar not found")
    
        # Return meetings that are associated with this calendar.
        return Meeting.objects.filter(calendar=calendar)

