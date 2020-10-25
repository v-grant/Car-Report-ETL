import io
from django.shortcuts import render, redirect
from .forms import CarReportForm, DataViewForm
from .models import CrashReport
from datetime import datetime
import datetime
from django.views.static import serve
from django.contrib import messages
from django.views.generic import View
from reportlab.pdfgen import canvas
import pdfplumber
import reportlab


class CrashReportViews(View):
    def get(self, request, *args, **kwargs):
        queryset = CrashReport.objects.all()
        queryset = {"queryset": queryset}
        return render(request, "data_report.html", queryset)


class DataReport(View):
    def get(self, request, *args, **kwargs):
        form = CarReportForm()
        return render(request, "car_report.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = CarReportForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "car_report.html", {"form": form})


def scrap_data(file_data):

    pdf = pdfplumber.open(file_data)

    page = pdf.pages[0]
    crcn = page.extract_text()[66:73]

    dict = {}
    dict2 = {}
    for c1, table in enumerate(page.extract_tables()):
        for c2, list in enumerate(table):
            for c3, x in enumerate(list):
                if x != None:
                    d = {"crash_report_case_no": crcn}
                    dict.update(d)
                    if c1 == 2 and c2 == 0 and c3 == 0:
                        d = {"local_case_no": x[15:]}
                        dict.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 3:
                        d = {"date_month": x}
                        dict.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 4:
                        d = {"date_day": x}
                        dict.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 8:
                        d = {"date_year": x}
                        dict.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 13:
                        d = {"time": x[5:]}
                        dict.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 21:
                        d = {"day_of_week": x[12:]}
                        dict.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 26:
                        d = {"county": x[7:]}
                        dict.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 38:
                        d = {"city": x[11:]}
                        dict.update(d)
                    if c1 == 0 and c2 == 7 and c3 == 2:
                        d = {"Drivers_full_name_Street_Address_City_and_State": x[47:]}
                        dict.update(d)
                    if c1 == 0 and c2 == 7 and c3 == 46:
                        d = {"zipcode": x[4:]}
                        dict.update(d)
                    if c1 == 0 and c2 == 7 and c3 == 50:
                        d = {"telephone": x[10:]}
                        dict.update(d)
                    if c1 == 0 and c2 == 8 and c3 == 3:
                        d = {"Date_Month": x}
                        dict.update(d)
                    if c1 == 0 and c2 == 8 and c3 == 4:
                        d = {"DOB_Day": x}
                        dict.update(d)
                    if c1 == 0 and c2 == 8 and c3 == 8:
                        d = {"DOB_Year": x}
                        dict.update(d)
                    if c1 == 0 and c2 == 8 and c3 == 12:
                        d = {"race": x[5:]}
                        dict.update(d)
                    if c1 == 0 and c2 == 8 and c3 == 15:
                        d = {"sex": x[4:]}
                        dict.update(d)
                    if c1 == 0 and c2 == 8 and c3 == 16:
                        d = {"dL_state": x[9:]}
                        dict.update(d)
                    if c1 == 0 and c2 == 8 and c3 == 20:
                        d = {"driving_license_no": x[19:]}
                        dict.update(d)
                    d = {"crash_report_case_no": crcn}
                    dict2.update(d)
                    if c1 == 2 and c2 == 0 and c3 == 0:
                        d = {"local_case_no": x[15:]}
                        dict2.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 3:
                        d = {"Date_Month": x}
                        dict2.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 4:
                        d = {"Date_Day": x}
                        dict2.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 8:
                        d = {"Date_year": x}
                        dict2.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 13:
                        d = {"time": x[5:]}
                        dict2.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 21:
                        d = {"day_of_week": x[12:]}
                        dict2.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 26:
                        d = {"county": x[7:]}
                        dict2.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 38:
                        d = {"city": x[11:]}
                        dict2.update(d)
                    if c1 == 0 and c2 == 24 and c3 == 2:
                        d = {"Drivers_full_name_Street_Address_City_and_State": x[47:]}
                        dict2.update(d)
                    if c1 == 0 and c2 == 24 and c3 == 46:
                        d = {"zipcode": x[4:]}
                        dict2.update(d)
                    if c1 == 0 and c2 == 24 and c3 == 50:
                        d = {"telephone": x[10:]}
                        dict2.update(d)
                    if c1 == 0 and c2 == 25 and c3 == 3:
                        d = {"DOB_Month": x}
                        dict2.update(d)
                    if c1 == 0 and c2 == 25 and c3 == 4:
                        d = {"DOB_Day": x}
                        dict2.update(d)
                    if c1 == 0 and c2 == 25 and c3 == 8:
                        d = {"DOB_Year": x}
                        dict2.update(d)
                    if c1 == 0 and c2 == 25 and c3 == 12:
                        d = {"race": x[5:]}
                        dict2.update(d)
                    if c1 == 0 and c2 == 25 and c3 == 15:
                        d = {"sex": x[4:]}
                        dict2.update(d)
                    if c1 == 0 and c2 == 25 and c3 == 16:
                        d = {"dL_state": x[9:]}
                        dict2.update(d)
                    if c1 == 0 and c2 == 25 and c3 == 20:
                        d = {"driving_license_no": x[19:]}
                        dict2.update(d)
    return dict2


def nu(num1, num2):
    digits = len(str(num2))
    num1 = num1 * (10 ** digits)
    num1 += num2
    return num1


def parse_pdf(request):
    if request.method == "POST":
        file_attached = request.FILES["filename"]._name
        data = scrap_data(request.FILES["filename"])
        month = int(data.get("Date_Month"))
        day = int(data.get("Date_Day"))
        year = int(data.get("Date_year"))
        data_date = datetime.datetime.strptime(str(nu(year, nu(day, month))), "%Y%d%m")
        pk = CrashReport.objects.create(
            crash_report_case_no=data["crash_report_case_no"],
            local_case_no=data["local_case_no"],
            date=data_date,
            time=data["time"],
            day_of_week=data["day_of_week"],
            county=data["county"],
            city=data["city"],
            Drivers_full_name_Street_Address_City_and_State=data[
                "Drivers_full_name_Street_Address_City_and_State"
            ],
            zipcode=data["zipcode"],
            telephone=data["telephone"],
            dob=data["DOB_Day"] + data["Date_Month"] + data["DOB_Year"],
            race=data["race"],
            sex=data["sex"],
            dL_state=data["dL_state"],
            driving_license_no=data["driving_license_no"],
            file_attached=file_attached,
        )
        messages.success(request, f"Scraped and saved successfully!")
        return redirect("car-report")
    return render(request, "data_report.html")
