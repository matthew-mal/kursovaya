from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from schedule import views

app_name = 'schedule'

urlpatterns = [
                  path('', views.schedule_list, name='schedule_list'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
