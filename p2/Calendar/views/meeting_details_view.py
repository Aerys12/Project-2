from rest_framework import generics
from Calendar.models.meeting import Meeting
from ..serializers.meeting_serializer import MeetingSerializer
from ..permissions import IsOwner


class MeetingDetailsView(generics.RetrieveAPIView):
    """
    API view for retrieving details of a meeting.

    This view retrieves the details of a meeting based on the provided meeting ID.
    Only the owner of the meeting has permission to access this view.

    Attributes:
        queryset (QuerySet): The queryset of all Meeting objects.
        serializer_class (Serializer): The serializer class for the Meeting model.
        permission_classes (list): The list of permission classes for this view.
        lookup_field (str): The field to use for the lookup.
        lookup_url_kwarg (str): The URL keyword argument to use for the lookup.
    """
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    permission_classes = [IsOwner]
    lookup_field = 'id'
    lookup_url_kwarg = 'meeting_id'
