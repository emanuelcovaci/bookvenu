from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['date_created','id','user','body']

admin.site.register(Contact, ContactAdmin)