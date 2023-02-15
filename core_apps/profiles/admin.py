from django.contrib import admin

from core_apps.profiles.models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display =['pkid','id','user','gender','country','city','phone_number']
    list_filter = ['gender','country','city']
    list_display_links = ['pkid','id']
    
admin.site.register(Profile,ProfileAdmin)