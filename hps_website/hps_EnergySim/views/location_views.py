from django.shortcuts import render, get_object_or_404, HttpResponse
from ..models import DutyCycle, OperatingSchedule
from hps_EnergySim.forms import (
    OperatingScheduleForm,
    OperatingScheduleLoadsForm,
    LocationForm,
)
from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from django_htmx.http import trigger_client_event


def locations(request, duty_cycle_id):
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

            response = render(
                request,
                "hps_EnergySim/partials/_submit_location.html",
                context,
            )
            trigger_client_event(response, "update-operating_schedules", {})
            return response

    locations = duty_cycle.location_set.all()

    form = LocationForm()
    locations.form = form

    context = {
        "duty_cycle": duty_cycle,
        "locations": locations,
    }
    return render(request, "hps_EnergySim/locations.html", context)


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

            response = render(
                request,
                "hps_EnergySim/partials/_submit_location.html",
                context,
            )
            trigger_client_event(response, "update-operating_schedules", {})
            return response
    else:
        return HttpResponseNotAllowed(["POST"])
