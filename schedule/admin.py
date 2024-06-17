from django.contrib import admin
from .models import Route, Schedule, Station, TimeSlot, Vessel


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_point', 'end_point', 'departure_time', 'arrival_time', 'interval']
    list_filter = ['name']


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ['route', 'name']
    list_filter = ['route']


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ['station', 'departure_time']
    list_filter = ['station']


@admin.register(Vessel)
class VesselAdmin(admin.ModelAdmin):
    list_display = ['name', 'route']
    list_filter = ['route']