from django.db import models

class Availability(models.Model):
    date_time = models.DateTimeField()
    calendar = models.ForeignKey('Calendar', related_name='availability_calendar', on_delete=models.CASCADE)
    preference = models.IntegerField()

    def __str__(self):
        return f'{self.date_time}'