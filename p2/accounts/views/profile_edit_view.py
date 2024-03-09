
from django.http.response import HttpResponse as HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView
from accounts.forms.profile_edit_form import ProfileEditForm
from django.contrib.auth import update_session_auth_hash

class ProfileEditView(FormView):
    template_name = 'accounts/profile.html'
    form_class = ProfileEditForm
    success_url = reverse_lazy('accounts:profile_view')
    

    def dispatch(self, request, *args, **kwargs) -> HttpResponse:
        if not request.user.is_authenticated:
            return HttpResponse('UNAUTHORIZED', status=401)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = self.request.user
        user = self.request.user
        if 'password1' in form.cleaned_data and form.cleaned_data['password1'] != "":
            if ('password2' not in form.cleaned_data) or form.cleaned_data['password1'] != form.cleaned_data['password2']:
                context = self.get_context_data()
                context['error_message'] = "The two password fields didn't match"
                return self.render_to_response(context)
            else:
                if len(form.cleaned_data['password1']) < 8:
                    context = self.get_context_data()
                    context['error_message'] = "This password is too short. It must contain at least 8 characters"
                    return self.render_to_response(context)
                else:
                    user.set_password(form.cleaned_data['password1'])

        if 'email' in form.cleaned_data:
            if '@' in form.cleaned_data['email'] or form.cleaned_data['email'] == "":
                user.email = form.cleaned_data['email']
            else:
                context = self.get_context_data()
                context['error_message'] = "Enter a valid email address."
                return self.render_to_response(context)
        if 'first_name' in form.cleaned_data:
            user.first_name = form.cleaned_data['first_name']

        if 'last_name' in form.cleaned_data:
            user.last_name = form.cleaned_data['last_name']

        user.save()
        update_session_auth_hash(self.request, user)
        return super().form_valid(form)

    def get_initial(self):
        user = self.request.user
        return {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        }
