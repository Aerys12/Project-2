from django.contrib import admin
from .models import availability
from .models import calendar


# Register your models here.
admin.site.register(availability)
admin.site.register(calendar)
admin.site.register(meeting)