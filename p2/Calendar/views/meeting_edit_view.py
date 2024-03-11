from rest_framework import generics, status
from Calendar.models.meeting import Meeting
from Calendar.models.calendar import Calendar
from ..serializers.meeting_serializer import MeetingSerializer
from ..permissions import IsOwner
from rest_framework.exceptions import NotFound
from Calendar import permissions


class MeetingEditView(generics.UpdateAPIView):
    """
    A view for updating a meeting instance.

    This view allows the owner of the meeting to update its details.
    Only the creator of the calendar associated with the meeting can perform the update.

    Attributes:
        queryset (QuerySet): The queryset of all Meeting objects.
        serializer_class (Serializer): The serializer class for the Meeting model.
        permission_classes (list): The list of permission classes for the view.
        lookup_field (str): The field to use for the lookup of the meeting.
        lookup_url_kwarg (str): The URL keyword argument for the lookup of the meeting.

    Methods:
        perform_update(serializer): Performs the update of the meeting instance.
    """

    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = [IsOwner]
    lookup_field = 'id'
    lookup_url_kwarg = 'meeting_id'

    def perform_update(self, serializer):
        """
        Performs the update of the meeting instance.

        Args:
            serializer (Serializer): The serializer instance for the meeting.

        Raises:
            NotFound: If the associated calendar is not found.
            PermissionDenied: If the user does not have permission to edit the meeting.

        Returns:
            None
        """
        calendar_id = self.kwargs.get('calendar_id')
        try:
            calendar = Calendar.objects.get(pk=calendar_id)
        except Calendar.DoesNotExist:
            raise NotFound(detail="Calendar not found", code=status.HTTP_404_NOT_FOUND)
        
        if not self.request.user == calendar.creator:
            raise permissions.exceptions.PermissionDenied(detail="You do not have permission to edit this meeting")
        
        serializer.save()
