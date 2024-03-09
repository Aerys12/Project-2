from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

class Logout(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('accounts:login'))
        return super().dispatch(request, *args, **kwargs)
      
    def get_next_page(self):
        return reverse_lazy('accounts:login')
    