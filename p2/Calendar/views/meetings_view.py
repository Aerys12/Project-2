# meetings_view.py

from rest_framework import generics
from Calendar.models.meeting import Meeting
from ..serializers.meeting_serializer import MeetingSerializer
from ..permissions import IsOwner

class MeetingsView(generics.ListAPIView):
    serializer_class = MeetingSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        # each user can only access their own meetings
        user = self.request.user
        return Meeting.objects.filter(creator=user)
