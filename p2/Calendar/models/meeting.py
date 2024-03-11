from django.db import models

class Meeting(models.Model):
    """
    Represents a meeting in the calendar.

    Attributes:
        title (str): The title of the meeting.
        receiver (str): The receiver of the meeting.
        status (bool): The status of the meeting.
        start_time (datetime): The start time of the meeting.
        calendar (Calendar): The calendar to which the meeting belongs.
    """

    title = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    start_time = models.DateTimeField(null=True)
    calendar = models.ForeignKey('Calendar', related_name='meeting_calendar', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
