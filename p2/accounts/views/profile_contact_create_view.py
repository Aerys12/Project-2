from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from accounts.serializers.contact_serializer import ContactSerializer  


class ContactCreateView(APIView):
    """
    API view for creating a new contact.

    This view handles the POST request to create a new contact using the ContactSerializer.
    If the serializer is valid, the contact is saved and a response with the serialized data
    and status code 201 (Created) is returned. If the serializer is not valid, a response
    with the serializer errors and status code 400 (Bad Request) is returned.
    """
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)