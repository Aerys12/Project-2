from rest_framework import generics
from Calendar.models.meeting import Meeting
from ..permissions import IsOwner

class MeetingDeletionView(generics.DestroyAPIView):
    """
    A view for deleting a meeting.

    Inherits from `generics.DestroyAPIView` class provided by Django REST Framework.
    Deletes a meeting object based on the specified meeting ID.

    Attributes:
        queryset (QuerySet): The queryset of all Meeting objects.
        permission_classes (list): The list of permission classes for the view.
        lookup_field (str): The field used to look up the meeting object.
        lookup_url_kwarg (str): The URL keyword argument used to retrieve the meeting ID.
    """
    queryset = Meeting.objects.all()
    permission_classes = [IsOwner]
    lookup_field = 'id'
    lookup_url_kwarg = 'meeting_id'
