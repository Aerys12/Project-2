from .views import login_view, register_view, logout_view, profile_details, profile_edit_view
from django.urls import path

app_name = 'accounts'
urlpatterns = [
    path('login/', login_view.LoginView.as_view() , name='login'),
    path('register/', register_view.RegisterView.as_view() , name='register'),
    path('logout/', logout_view.LogoutView.as_view() , name='logout'),
    path('profile/details/', profile_details.ProfileDetailsView.as_view() , name='profile_details'),
    path('profile/edit/', profile_edit_view.ProfileEditView.as_view() , name='edit'),
]