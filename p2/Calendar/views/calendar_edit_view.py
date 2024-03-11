from rest_framework.generics import UpdateAPIView
from ..serializers.calendar_serializer import CalendarUpdateSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..permissions import IsOwnerOrReadOnly
from ..models.calendar import Calendar


class CalendarUpdateView(UpdateAPIView):
    """
    A view for updating a calendar object.

    This view allows authenticated users to update a calendar object.
    Only the owner of the calendar object can perform the update.

    Attributes:
        queryset (QuerySet): The queryset of Calendar objects.
        serializer_class (Serializer): The serializer class for updating a calendar object.
        permission_classes (list): The list of permission classes for the view.
        lookup_field (str): The field to use for looking up the calendar object.
        lookup_url_kwarg (str): The URL keyword argument for the lookup field.
    """
    queryset = Calendar.objects.all()
    serializer_class = CalendarUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = "id"
    lookup_url_kwarg = 'calendar_id'
