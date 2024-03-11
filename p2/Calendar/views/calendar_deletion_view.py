from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from ..models.calendar import Calendar
from ..permissions import IsOwnerOrReadOnly

class CalendarDeleteView(DestroyAPIView):
    """
    A view for deleting a calendar object.

    Inherits from DestroyAPIView which provides a DELETE method handler.
    Requires authentication and permission to delete the calendar object.
    The calendar object is identified by the 'id' field in the URL.

    Attributes:
        queryset (QuerySet): The queryset of Calendar objects.
        permission_classes (list): The list of permission classes required for the view.
        lookup_field (str): The field used to look up the calendar object.
        lookup_url_kwarg (str): The URL keyword argument used to retrieve the calendar ID.
    """
    queryset = Calendar.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'id'
    lookup_url_kwarg = 'calendar_id'
