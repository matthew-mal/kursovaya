from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('water-tram/', include('schedule.urls', namespace='schedule')),
]
