from django.shortcuts import render, get_object_or_404, HttpResponse
from ..models import DutyCycle, OperatingSchedule
from hps_EnergySim.forms import OperatingScheduleForm, OperatingScheduleLoadsForm, LocationForm
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest


def add_location(request, duty_cycle_id):
    duty_cycle = get_object_or_404(DutyCycle, pk=duty_cycle_id)

    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.duty_cycle = duty_cycle
            location.save()
            form.save_m2m()

            form = LocationForm()

            locations = {"form": form}

            context = {
                "duty_cycle": duty_cycle,
                "locations": locations,
                "location": location,
            }

            return render(
                request,
                "hps_EnergySim/partials/_submit_location.html",
                context,
            )
    else:
        return HttpResponseNotAllowed(["POST"])