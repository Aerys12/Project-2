from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class RegisterView(APIView):
    """
    API view for user registration.

    This view handles the registration of a new user by receiving a POST request
    with the following parameters:
    - username: The desired username for the new user.
    - password1: The password for the new user.
    - password2: The confirmation password for the new user.
    - email: The email address for the new user.
    - first_name: The first name of the new user.
    - last_name: The last name of the new user.

    If any of the required fields are missing or the passwords do not match,
    an error response is returned. Otherwise, a new user is created and a success
    response is returned.

    HTTP Methods:
    - POST: Create a new user.

    Returns:
    - 201 Created: If the user is created successfully.
    - 400 Bad Request: If any of the required fields are missing or the passwords do not match.
    """

    def post(self, request):
        username = request.data.get('username')
        password1 = request.data.get('password1')
        password2 = request.data.get('password2')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        if not username or not password1 or not password2 or not email:
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)
        if password1 != password2:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)