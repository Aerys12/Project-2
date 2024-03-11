from django.db import models

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    start_time = models.DateTimeField(null=True)
    calendar = models.ForeignKey('Calendar', related_name='meeting_calendar', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
