from django.contrib import admin
from .models import Project, DutyCycle, Location, OperatingSchedule, OperatingLoad

admin.site.register(Project)
admin.site.register(DutyCycle)
admin.site.register(Location)
admin.site.register(OperatingSchedule)
admin.site.register(OperatingLoad)
