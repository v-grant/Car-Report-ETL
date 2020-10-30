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
    file_attached = models.FileField(upload_to="files/", null=True, verbose_name="")

    def __str__(self):
        return self.crash_report_case_no

    @property
    def drivers(self):
        try:
            return CrashDrivers.objects.filter(crash_report_case_no=self.crash_report_case_no)
        except:
            return []

class CrashDrivers(models.Model):
    crash_report_case_no = models.CharField(max_length=20)
    Drivers_full_name = models.CharField(max_length=255, null=True)
    Street_Address_City_and_State = models.CharField(max_length=255, null=True)
    zipcode = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    dob = models.CharField(max_length=100)
    race = models.CharField(max_length=20)
    sex = models.CharField(max_length=10)
    dL_state = models.CharField(max_length=35)
    driving_license_no = models.CharField(max_length=15)

    @property
    def crash_report(self):
        try:
            return CrashReport.objects.get(crash_report_case_no=self.crash_report_case_no)
        except:
            return None


class RequestReport(models.Model):
    search_result_choices = ( 
        ("0", "Not Existing"), 
        ("1", "Necessary"), 
        ("2", "Old Report"), 
        ("3", "Single Car Accident"), 
        ("4", "Both Of Reasons"), 
    )   
    crash_report_num = models.CharField(max_length=100, null=True, blank=True)
    crash_date = models.CharField(max_length=100, null=True, blank=True)
    driver_name = models.CharField(max_length=100, null=True, blank=True)
    county = models.CharField(max_length=100, null=True, blank=True)
    search_date =  models.CharField(max_length=100, null=True, blank=True)
    search_result = models.CharField(max_length=1, choices = search_result_choices, null=True, blank=True)
    inserted_date = models.DateTimeField(auto_now_add=True, blank=True)    
    updatd_date = models.DateTimeField(auto_now=True, blank=True)