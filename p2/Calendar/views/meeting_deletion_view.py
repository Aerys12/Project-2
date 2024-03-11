# meeting_deletion_view.py

from rest_framework import generics
from Calendar.models.meeting import Meeting
from ..permissions import IsOwner

class MeetingDeletionView(generics.DestroyAPIView):
    queryset = Meeting.objects.all()
    permission_classes = [IsOwner]
    lookup_field = 'id'
    lookup_url_kwarg = 'meeting_id'
