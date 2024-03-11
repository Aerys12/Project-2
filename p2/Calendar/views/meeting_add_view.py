from rest_framework import generics, status
from rest_framework.response import Response
from Calendar.models.meeting import Meeting
from Calendar.models.calendar import Calendar
from ..serializers.meeting_serializer import MeetingSerializer
from ..permissions import IsOwner
from rest_framework.exceptions import NotFound


class MeetingAddView(generics.CreateAPIView):
    """
    A view for adding a new meeting to a calendar.

    This view allows authenticated users to create a new meeting and associate it with a specific calendar.
    The user must be the owner of the calendar in order to add a meeting.

    Attributes:
        queryset (QuerySet): The queryset of all Meeting objects.
        serializer_class (Serializer): The serializer class for the Meeting model.
        permission_classes (list): The list of permission classes for the view.

    Methods:
        perform_create(serializer): Performs the creation of a new meeting and associates it with the calendar.
    """
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        """
        Performs the creation of a new meeting and associates it with the calendar.

        Args:
            serializer (Serializer): The serializer instance for the Meeting model.

        Raises:
            NotFound: If the specified calendar does not exist.

        Returns:
            None
        """
        calendar_id = self.kwargs.get('calendar_id')
        try:
            calendar = Calendar.objects.get(pk=calendar_id, creator=self.request.user)
        except Calendar.DoesNotExist:
            raise NotFound(detail="Calendar not found", code=status.HTTP_404_NOT_FOUND)
        
        serializer.save(calendar=calendar)

