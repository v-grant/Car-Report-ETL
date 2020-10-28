from django.db import models
from django.conf import settings
from django.utils import timezone


class CrashReport(models.Model):
    crash_report_case_no = models.CharField(max_length=20)
    local_case_no = models.CharField(max_length=15)
    date = models.CharField(max_length=500)
    time = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=50)
    county = models.CharField(max_length=35)
    city = models.CharField(max_length=35)
    rural = models.BooleanField(null=True, blank=True)
    Drivers_full_name = models.CharField(max_length=255, null=True)
    Street_Address_City_and_State = models.CharField(max_length=255, null=True)
    zipcode = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    dob = models.CharField(max_length=100)
    race = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    dL_state = models.CharField(max_length=35)
    driving_license_no = models.CharField(max_length=15)
    file_attached = models.FileField(upload_to="files/", null=True, verbose_name="")

    def __str__(self):
        return self.crash_report_case_no


class RequestReport(models.Model):
    report_num = models.CharField(max_length=100)
    request_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.reportnum
        self.save()