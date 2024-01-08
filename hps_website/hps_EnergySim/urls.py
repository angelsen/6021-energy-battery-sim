from django.urls import path
from . import views

urlpatterns = [
    path('duty_cycle/<int:duty_cycle_id>/', views.duty_cycle_detail, name='duty_cycle_detail'),
    path('operating-schedules-loads/<int:operating_schedule_id>/<int:duty_cycle_id>', views.operating_schedule_loads, name='operating_schedules_load'),
    path('add_operating_schedule/<int:duty_cycle_id>/', views.add_operating_schedule, name='add_operating_schedule'),
    path('add_location/<int:duty_cycle_id>/', views.add_location, name='add_location'),
]