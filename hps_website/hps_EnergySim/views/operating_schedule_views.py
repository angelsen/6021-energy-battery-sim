from django.shortcuts import render, get_object_or_404, HttpResponse
from ..models import DutyCycle, OperatingSchedule
from hps_EnergySim.forms import OperatingScheduleForm, OperatingScheduleLoadsForm
from django.http import HttpResponseNotAllowed


def delete_operating_schedules(request, duty_cycle_id, operating_schedule_id):
    duty_cycle = get_object_or_404(DutyCycle, pk=duty_cycle_id)
    operating_schedules = duty_cycle.operatingschedule_set.all()

    if request.method == "DELETE":
        operating_schedule = get_object_or_404(
            duty_cycle.operatingschedule_set, pk=operating_schedule_id
        )
        operating_schedule.delete()

        last_schedule = duty_cycle.operatingschedule_set.last()

        if last_schedule:
            form = OperatingScheduleForm(
                initial={
                    "start_time": last_schedule.end_time,
                    "end_time": last_schedule.end_time,
                }
            )
        else:
            form = OperatingScheduleForm()

        operating_schedules.form = form

        context = {
            "duty_cycle": duty_cycle,
            "operating_schedules": operating_schedules,
        }
        return render(
            request, "hps_EnergySim/partials/_submit_operating_schedule.html", context
        )


def operating_schedules(request, duty_cycle_id):
    duty_cycle = get_object_or_404(DutyCycle, pk=duty_cycle_id)

    if request.method == "POST":
        form = OperatingScheduleForm(request.POST)
        if form.is_valid():
            operating_schedule = form.save(commit=False)
            operating_schedule.duty_cycle = duty_cycle
            operating_schedule.save()
            form.save_m2m()

            form = OperatingScheduleLoadsForm(instance=operating_schedule)
            form.fields["operating_loads"].widget.attrs[
                "id"
            ] = f"id_operating_loads_{operating_schedule.id}"
            operating_schedule.form = form

            form = OperatingScheduleForm()
            form.fields["start_time"].initial = operating_schedule.end_time
            form.fields["end_time"].initial = operating_schedule.end_time

            operating_schedules = {"form": form}

            context = {
                "duty_cycle": duty_cycle,
                "operating_schedules": operating_schedules,
                "operating_schedule": operating_schedule,
            }

            return render(
                request,
                "hps_EnergySim/partials/_submit_operating_schedule.html",
                context,
            )

    operating_schedules = duty_cycle.operatingschedule_set.prefetch_related(
        "operating_loads"
    ).all()

    for operating_schedule in operating_schedules:
        form = OperatingScheduleLoadsForm(instance=operating_schedule)
        form.fields["operating_loads"].widget.attrs[
            "id"
        ] = f"id_operating_loads_{operating_schedule.id}"
        operating_schedule.form = form

    form = OperatingScheduleForm()
    last_schedule = operating_schedules.last()
    if last_schedule is not None:
        form.fields["start_time"].initial = last_schedule.end_time
        form.fields["end_time"].initial = last_schedule.end_time
    operating_schedules.form = form

    context = {
        "duty_cycle": duty_cycle,
        "operating_schedules": operating_schedules,
    }
    return render(request, "hps_EnergySim/operating_schedules.html", context)


def operating_schedule_loads(request, duty_cycle_id, operating_schedule_id):
    operating_schedule = get_object_or_404(OperatingSchedule, pk=operating_schedule_id)

    if request.method == "POST":
        form = OperatingScheduleLoadsForm(request.POST, instance=operating_schedule)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204)
    else:
        return HttpResponseNotAllowed(["POST"])
