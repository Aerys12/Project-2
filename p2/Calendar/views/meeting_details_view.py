from rest_framework import generics
from Calendar.models.meeting import Meeting
from ..serializers.meeting_serializer import MeetingSerializer
from ..permissions import IsOwner

class MeetingDetailsView(generics.RetrieveAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = [IsOwner]
    lookup_field = 'id'
    lookup_url_kwarg = 'meeting_id'
