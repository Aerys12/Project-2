from rest_framework.generics import RetrieveAPIView
from ..serializers.calendar_serializer import CalendarViewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..models.calendar import Calendar


class CalendarDetailsView(RetrieveAPIView):
    """
    A view for retrieving details of a calendar.

    This view allows anyone to view the details of a calendar by providing the calendar ID in the URL.

    Attributes:
        queryset (QuerySet): The queryset of Calendar objects to retrieve from.
        serializer_class (Serializer): The serializer class to use for serializing the retrieved calendar object.
        lookup_field (str): The field to use for looking up the calendar object.
        lookup_url_kwarg (str): The URL keyword argument to use for retrieving the calendar ID from the URL.
    """
    queryset = Calendar.objects.all()
    serializer_class = CalendarViewSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'calendar_id'



