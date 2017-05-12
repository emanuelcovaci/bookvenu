from django.contrib import admin
from .models import ThreadComment,Thread

# Register your models here.
class ThreadAdmin(admin.ModelAdmin):
    list_display = ['name', 'body','user','data_created']

admin.site.register(Thread, ThreadAdmin)

class ThreadCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'body']

admin.site.register(ThreadComment, ThreadCommentAdmin)