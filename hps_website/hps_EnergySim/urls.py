from django.urls import path
from . import views

urlpatterns = [
    path("duty-cycles/<int:duty_cycle_id>/", views.duty_cycles, name="duty_cycles"),
    path(
        "operating-schedules-loads/<int:operating_schedule_id>/<int:duty_cycle_id>",
        views.operating_schedule_loads,
        name="operating_schedules_load",
    ),
    path(
        "duty-cycles/<int:duty_cycle_id>/operating-schedules",
        views.operating_schedules,
        name="operating_schedules",
    ),
    path(
        "duty-cycles/<int:duty_cycle_id>/operating-schedules/<int:operating_schedule_id>",
        views.delete_operating_schedules,
        name="delete_operating_schedules",
    ),
    path(
        "duty-cycles/<int:duty_cycle_id>/locations", views.locations, name="locations"
    ),
    path(
        "duty-cycles/<int:duty_cycle_id>/operating-loads",
        views.operating_loads,
        name="operating_loads",
    ),
]
