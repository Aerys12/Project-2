from django.urls import path
from .views.calendar_create_view import CalendarCreateView
from .views.calendars_view import CalendarsView
from .views.calendar_edit_view import CalendarUpdateView
from .views.calendar_details_view import CalendarDetailsView
from .views.calendar_deletion_view import CalendarDeleteView

from .views.meeting_add_view import MeetingAddView
from .views.meeting_deletion_view import MeetingDeletionView
from .views.meeting_details_view import MeetingDetailsView
from .views.meeting_edit_view import MeetingEditView
from .views.meetings_view import MeetingsView


app_name = 'Calendar'
urlpatterns = [
    path('add/', CalendarCreateView.as_view(), name='calendar_add'),
    path('all/', CalendarsView.as_view(), name='calendars_all'),
    path('<int:calendar_id>/edit', CalendarUpdateView.as_view(), name='calendar_edit'),
    path('<int:calendar_id>/details', CalendarDetailsView.as_view(), name='calender_detail'),
    path('<int:calendar_id>/delete', CalendarDeleteView.as_view(), name='calendar_delete'),

    path('calendars/<int:calendar_id>/meetings/add/', MeetingAddView.as_view(), name='meeting_add'),
    path('calendars/<int:calendar_id>/meetings/<int:meeting_id>/delete/', MeetingDeletionView.as_view(), name='meeting_delete'),
    path('calendars/<int:calendar_id>/meetings/<int:meeting_id>/', MeetingDetailsView.as_view(), name='meeting_details'),
    path('calendars/<int:calendar_id>/meetings/<int:meeting_id>/edit/', MeetingEditView.as_view(), name='meeting_edit'),
    path('calendars/<int:calendar_id>/meetings/', MeetingsView.as_view(), name='meetings_all'),
]