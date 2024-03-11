from rest_framework.generics import UpdateAPIView
from ..serializers.calendar_serializer import CalendarUpdateSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..permissions import IsOwnerOrReadOnly
from ..models.calendar import Calendar


class CalendarUpdateView(UpdateAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = "id"
    lookup_url_kwarg = 'calendar_id'
