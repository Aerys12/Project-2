from rest_framework.generics import ListAPIView
from ..serializers.calendar_serializer import CalendarViewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..models.calendar import Calendar


class CalendarsView(ListAPIView):
    serializer_class = CalendarViewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Calendar.objects.filter(creator=user)
