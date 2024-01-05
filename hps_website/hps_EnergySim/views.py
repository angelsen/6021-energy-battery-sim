from django.shortcuts import render, get_object_or_404
from .models import DutyCycle, OperatingSchedule


def duty_cycle_detail(request, duty_cycle_id):
    duty_cycle = get_object_or_404(DutyCycle, pk=duty_cycle_id)
    locations = duty_cycle.location_set.all()
    operating_schedules = duty_cycle.operatingschedule_set.prefetch_related(
        "operating_loads"
    ).all()
    operating_loads = duty_cycle.operatingload_set.all()

    context = {
        "duty_cycle": duty_cycle,
        "locations": locations,
        "operating_schedules": operating_schedules,
        "operating_loads": operating_loads,
    }
    return render(request, "hps_EnergySim/duty_cycle.html", context)


def operating_schedules_loads(request, duty_cycle_id, operating_schedule_id):
    new_operating_loads = request.GET.getlist("operating_loads[]")

    duty_cycle = get_object_or_404(
        DutyCycle.objects.prefetch_related("operatingload_set"),
        pk=duty_cycle_id,
    )

    operating_schedule = get_object_or_404(OperatingSchedule, pk=operating_schedule_id)

    operating_schedule.operating_loads.set(new_operating_loads)

    operating_loads = duty_cycle.operatingload_set.all()

    context = {
        "operating_schedule": operating_schedule,
        "operating_loads": operating_loads,
        #"duty_cycle": duty_cycle,
    }

    return render(request, "hps_EnergySim/partials/_select_loads.html", context)
