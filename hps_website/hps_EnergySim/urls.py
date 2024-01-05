from django.urls import path
from . import views

urlpatterns = [
    path('duty_cycle/<int:duty_cycle_id>/', views.duty_cycle_detail, name='duty_cycle_detail'),
    path('operating-schedules-loads/<int:operating_schedule_id>/<int:duty_cycle_id>', views.operating_schedules_loads, name='operating_schedules_loads'),
]