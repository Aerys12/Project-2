from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from ..models.calendar import Calendar
from ..permissions import IsOwnerOrReadOnly


class CalendarDeleteView(DestroyAPIView):
    queryset = Calendar.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'id'
    lookup_url_kwarg = 'calendar_id'
