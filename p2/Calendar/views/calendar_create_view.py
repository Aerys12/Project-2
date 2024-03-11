from rest_framework.generics import CreateAPIView
from ..serializers.calendar_serializer import CalendarCreateSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class CalendarCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = CalendarCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
