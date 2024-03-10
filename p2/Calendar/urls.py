from django.urls import path
from Calendar.views import calendar_create_view

app_name = 'Calendar'
urlpatterns = [
    path('create/', calendar_create_view.CalendarCreateView.as_view(), name='create'),
]
