from django.urls import path
from .views.calendar_create_view import CalendarCreateView
from .views.calendars_view import CalendarsView
from .views.calendar_edit_view import CalendarUpdateView
from .views.calendar_details_view import CalendarDetailsView
from .views.calendar_deletion_view import CalendarDeleteView

app_name = 'Calendar'
urlpatterns = [
    path('add/', CalendarCreateView.as_view(), name='calendar_add'),
    path('all/', CalendarsView.as_view(), name='calendars_all'),
    path('<int:calendar_id>/edit', CalendarUpdateView.as_view(), name='calendar_edit'),
    path('<int:calendar_id>/details', CalendarDetailsView.as_view(), name='calender_detail'),
    path('<int:calendar_id>/delete', CalendarDeleteView.as_view(), name='calendar_delete'),
    # path('<int:calendar_id>/meetings/add/'),
    # path('<int:calendar_id>/meetings/<int:meeting_id>/details/'),
    # path('<int:calendar_id>/meetings/<int:meeting_id>/edit/'),
    # path('<int:calendar_id>/meetings/<int:meeting_id>/delete/'),
    # path('<int:calendar_id>/meetings/all/')
]
