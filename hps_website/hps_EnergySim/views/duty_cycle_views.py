from django.shortcuts import render, get_object_or_404, HttpResponse
from ..models import DutyCycle, OperatingSchedule
from hps_EnergySim.forms import OperatingScheduleForm, OperatingScheduleLoadsForm, LocationForm
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest


def duty_cycles(request, duty_cycle_id):
    duty_cycle = get_object_or_404(DutyCycle, pk=duty_cycle_id)

    locations = duty_cycle.location_set.all()

    form = LocationForm()
    locations.form = form

    context = {
        "duty_cycle": duty_cycle,
        "locations": locations,
    }
    return render(request, "hps_EnergySim/duty_cycle.html", context)
