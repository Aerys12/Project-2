from rest_framework.generics import ListAPIView
from ..serializers.calendar_serializer import CalendarViewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..models.calendar import Calendar


class CalendarsView(ListAPIView):
    """
    A view for retrieving calendars created by the authenticated user.
    """
    serializer_class = CalendarViewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Returns the queryset of calendars created by the authenticated user.
        """
        user = self.request.user
        return Calendar.objects.filter(creator=user)
