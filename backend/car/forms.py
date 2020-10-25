from django import forms

from .models import CrashReport


class CarReportForm(forms.ModelForm):
    class Meta:
        model = CrashReport
        fields = "__all__"


class DataViewForm(forms.ModelForm):
    class Meta:
        model = CrashReport
        fields = "__all__"
