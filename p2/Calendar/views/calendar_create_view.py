from rest_framework.generics import CreateAPIView
from ..serializers.calendar_serializer import CalendarCreateSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class CalendarCreateView(CreateAPIView):
    """
    API view for creating a new calendar.
    Requires authentication.
    """
    permission_classes = [IsAuthenticated]
    def post(self, request):
        """
        Create a new calendar.

        Parameters:
        - request: The HTTP request object.

        Returns:
        - Response object with the serialized calendar data if successful (HTTP 201).
        - Response object with the serializer errors if validation fails (HTTP 400).
        """
        serializer = CalendarCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
