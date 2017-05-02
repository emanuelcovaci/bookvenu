from django.contrib import admin
from models import RequestModel
# Register your models here.
class RequestModelAdmin(admin.ModelAdmin):
    list_display = ['city', 'details','date']

admin.site.register(RequestModel, RequestModelAdmin)