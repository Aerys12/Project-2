from accounts.forms.login_form import LoginForm
from django.contrib.auth import login  
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import authenticate  

class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('accounts:profile_view')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password) 
        print(f"user: {user}")
        if user is not None:
            response = super().form_valid(form)
            login(self.request, user)
            return response
            
        else:
            form.add_error(None, 'Username or password is invalid')
            return self.form_invalid(form)
        
        
