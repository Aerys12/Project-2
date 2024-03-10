from rest_framework.generics import RetrieveAPIView
from ..serializers.calendar_serializer import CalendarViewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..models.calendar import Calendar


class CalendarDetailsView(RetrieveAPIView):
    #anyone can view
    queryset = Calendar.objects.all()
    serializer_class = CalendarViewSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'calendar_id'



