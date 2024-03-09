from django.db import models

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    status = models.BooleanField()
    start_time = models.DateTimeField()
    calendar = models.ForeignKey('Calendar', related_name='meetings', on_delete=models.CASCADE)

    def __str__(self):
        return self.title