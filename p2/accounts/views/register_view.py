from accounts.forms.register_form import RegisterForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        self.request.session['form'] = 'register'  
        return super().form_valid(form)