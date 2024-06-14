from django.shortcuts import render
from .models import Route, Schedule


def schedule_list(request):
    schedules = Schedule.objects.all()

    return render(request, 'schedule_list.html', {'schedules': schedules})
