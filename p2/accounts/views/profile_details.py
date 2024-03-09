from django.http import JsonResponse
from django.views import View

class ProfileDetailsView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            data = {
                "id": user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,    
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'UNAUTHORIZED'}, status=401)