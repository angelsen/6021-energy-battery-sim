# forms.py
from django import forms
from django.forms.widgets import DateTimeInput
from .models import OperatingLoad, OperatingSchedule,  Location

class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = ["name"]

class OperatingScheduleForm(forms.ModelForm):
    operating_loads = forms.ModelMultipleChoiceField(
        queryset=OperatingLoad.objects.all(),
        widget=forms.SelectMultiple(
            attrs={"class": "js-operating-load-select", "disabled": True, "hidden": True}
        ),
        required=False,
    )

    class Meta:
        model = OperatingSchedule
        fields = ["start_time", "end_time", "location", "operating_loads"]
        widgets = {
            "start_time": DateTimeInput(
                attrs={"type": "datetime-local",}
            ),
            "end_time": DateTimeInput(
                attrs={"type": "datetime-local",}
            ),
            "location": forms.Select(
                attrs={"class": "js-operating-load-select", "disabled": True, "hidden": True}
            )
        }

class OperatingScheduleLoadsForm(forms.ModelForm):
    operating_loads = forms.ModelMultipleChoiceField(
        queryset=OperatingLoad.objects.all(),
        widget=forms.SelectMultiple(
            attrs={"class": "js-operating-load-select", "disabled": True, "hidden": True}
        ),
        required=False,
    )

    class Meta:
        model = OperatingSchedule
        fields = ["operating_loads"]
