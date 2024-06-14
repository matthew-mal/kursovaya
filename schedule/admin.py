from django.contrib import admin
from .models import Route, Schedule


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['name', 'departure_time', 'arrival_time']
    list_filter = ['name']
