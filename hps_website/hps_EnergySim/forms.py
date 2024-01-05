# forms.py
from django import forms
from .models import OperatingLoad, OperatingSchedule

class OperatingScheduleForm(forms.ModelForm):
    operating_loads = forms.ModelMultipleChoiceField(
        queryset=OperatingLoad.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'js-operating-load-select'}),
        required=False
    )

    class Meta:
        model = OperatingSchedule
        fields = ['operating_loads']