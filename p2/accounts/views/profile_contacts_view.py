from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  
from accounts.models.contact import Contact  
from accounts.serializers.contact_serializer import ContactSerializer  

class ContactListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        contacts = Contact.objects.filter(owner=request.user)
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)