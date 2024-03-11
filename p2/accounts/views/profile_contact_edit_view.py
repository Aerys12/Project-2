from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from accounts.models.contact import Contact  
from accounts.serializers.contact_serializer import ContactSerializer 

class ContactUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Contact.objects.get(pk=pk, owner=self.request.user)
        except Contact.DoesNotExist:
            return None

    def put(self, request, pk):
        contact = self.get_object(pk)
        if contact is None:
            return Response({'message': 'Contact not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        contact = self.get_object(pk)
        if contact is None:
            return Response({'message': 'Contact not found'}, status=status.HTTP_404_NOT_FOUND)
        contact.delete()
        return Response({'message': 'Contact deleted successfully'}, status=status.HTTP_200_OK)