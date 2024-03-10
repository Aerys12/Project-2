from rest_framework import generics
from Calendar.models.calendar import Calendar
from Calendar.serializers.calendar_serializer import CalendarSerializer
#from rest_framework.permissions import IsAuthenticated

class CalendarCreateView(generics.CreateAPIView):
    serializer_class = CalendarSerializer
    #permission_classes = [IsAuthenticated]
    #authentication_classes = [] # use this to allow unauthenticated access

