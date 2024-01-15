from django.shortcuts import render, get_object_or_404
from ..models import DutyCycle
from hps_EnergySim.forms import OperatingLoadForm
from django_htmx.http import trigger_client_event

def operating_loads(request, duty_cycle_id):
    duty_cycle = get_object_or_404(DutyCycle, pk=duty_cycle_id)

    if request.method == "POST":
        form = OperatingLoadForm(request.POST)
        if form.is_valid():
            operating_load = form.save(commit=False)
            operating_load.duty_cycle = duty_cycle
            operating_load.save()
            form.save_m2m()

            form = OperatingLoadForm()
            operating_loads = {"form": form}

            context = {
                "duty_cycle": duty_cycle,
                "operating_loads": operating_loads,
                "operating_load": operating_load,
            }

            response = render(
                request,
                "hps_EnergySim/partials/_submit_operating_loads.html",
                context,
            )
            trigger_client_event(response, "update-operating_schedules", {})
            return response
        
    operating_loads = duty_cycle.operatingload_set.all()

    form = OperatingLoadForm
    operating_loads.form = form
    
    context = {
        "duty_cycle": duty_cycle,
        "operating_loads": operating_loads,
    }

    return render(request, 'hps_EnergySim/operating_loads.html', context)