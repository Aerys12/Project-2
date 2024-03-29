from rest_framework.generics import CreateAPIView
from ..serializers.calendar_serializer import CalendarCreateSerializer
from rest_framework.permissions import IsAuthenticated
from ..models.calendar import Calendar

class CalendarCreateView(CreateAPIView):
    """
    View for creating a new calendar.
    """
    permission_classes = [IsAuthenticated]
    queryset = Calendar.objects.all()
    serializer_class = CalendarCreateSerializer

    def perform_create(self, serializer):
        """
        Perform the creation of a new calendar.
        """
        serializer.save(creator=self.request.user)
