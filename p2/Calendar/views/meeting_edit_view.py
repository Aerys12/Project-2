# meeting_edit_view.py

from rest_framework import generics, status
from Calendar.models.meeting import Meeting
from Calendar.models.calendar import Calendar
from ..serializers.meeting_serializer import MeetingSerializer
from ..permissions import IsOwner
from rest_framework.exceptions import NotFound
from Calendar import permissions


class MeetingEditView(generics.UpdateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = [IsOwner]
    lookup_field = 'id'
    lookup_url_kwarg = 'meeting_id'

    def perform_update(self, serializer):
        calendar_id = self.kwargs.get('calendar_id')
        try:
            calendar = Calendar.objects.get(pk=calendar_id)
        except Calendar.DoesNotExist:
            raise NotFound(detail="Calendar not found", code=status.HTTP_404_NOT_FOUND)
        
        if not self.request.user == calendar.creator:
            raise permissions.exceptions.PermissionDenied(detail="You do not have permission to edit this meeting")
        
        serializer.save()
