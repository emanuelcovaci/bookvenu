from django.contrib import admin
from models import EventModel,Comment


class EventModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'details','category','date']

admin.site.register(EventModel, EventModelAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'body']

admin.site.register(Comment, CommentAdmin)