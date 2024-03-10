from django.db import models


class Calendar(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    duration = models.IntegerField()
    creator = models.ForeignKey('auth.User', related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
