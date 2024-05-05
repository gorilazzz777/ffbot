from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'name')
    list_filter = ('date', 'name')


admin.site.register(User, UserAdmin)
admin.site.register(Event, EventAdmin)