from rest_framework.generics import CreateAPIView
from ..serializers.calendar_serializer import CalendarCreateSerializer
from rest_framework.permissions import IsAuthenticated
from ..models.calendar import Calendar


class CalendarCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Calendar.objects.all()
    serializer_class = CalendarCreateSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
