from django.contrib import admin
from models import EventModel


class EventModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'details','category','date']

admin.site.register(EventModel, EventModelAdmin)