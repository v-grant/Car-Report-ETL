from django import forms

from .models import CrashReport
from .models import RequestReport


class CarReportForm(forms.ModelForm):
    class Meta:
        model = CrashReport
        fields = "__all__"


class DataViewForm(forms.ModelForm):
    class Meta:
        model = CrashReport
        fields = "__all__"

class RequestReportForm(forms.ModelForm):
    class Meta:
        model = RequestReport
        fields = "__all__"
