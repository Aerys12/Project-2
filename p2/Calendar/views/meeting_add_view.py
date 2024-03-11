from rest_framework import generics, status
from rest_framework.response import Response
from Calendar.models.meeting import Meeting
from Calendar.models.calendar import Calendar
from ..serializers.meeting_serializer import MeetingSerializer
from ..permissions import IsOwner
from rest_framework.exceptions import NotFound


class MeetingAddView(generics.CreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        calendar_id = self.kwargs.get('calendar_id')
        try:
            calendar = Calendar.objects.get(pk=calendar_id, creator=self.request.user)
        except Calendar.DoesNotExist:
            raise NotFound(detail="Calendar not found", code=status.HTTP_404_NOT_FOUND)
        
        serializer.save(calendar=calendar)

