from django.urls import path
from schedule import views

app_name = 'schedule'

urlpatterns = [
    path('', views.schedule_list, name='schedule_list'),
]