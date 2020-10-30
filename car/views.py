import io
from django.shortcuts import render, redirect
from .forms import CarReportForm, DataViewForm, RequestReportForm
from .models import CrashReport, RequestReport
from datetime import datetime
from django.views.static import serve
from django.contrib import messages
from django.views.generic import View
from reportlab.pdfgen import canvas
from bs4 import BeautifulSoup

import reportlab

from script.pdf_parser import scrap_data
from script.generate_report import request_report
import time 

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

class RequestReportView(View):
    def get(self, request, *args, **kwargs):
        reports = RequestReport.objects.all()
        return render(request, "Request_report.html", {"reports": reports})
    
    def post(self, request, *args, **kwargs):
        cr_number = request.POST.get('cr_number')

        #run selenium to fetch the crach report
        results = request_report(cr_number)
        driver_name = ''
        search_result_type = '0'
        is_one_line = False
        is_date_expired = False
        if len(results) > 0:
            if len(results) == 1:
                is_one_line = True
            cr_date = results[0]['Crash_Date']
            cr_timestamp = time.mktime(datetime.strptime(cr_date, "%m/%d/%Y").timetuple())
            now_timestamp = time.time()
            if((now_timestamp - cr_timestamp) > (7 * 3600 * 24)):
                is_date_expired = True
            for result in results:
                driver_name = f'({result["Name"]})' if driver_name == '' else f'{driver_name} ({result["Name"]})'
            
            if is_one_line == True and is_date_expired == True:
                search_result_type ='4'
            elif is_one_line == True:
                search_result_type = '3'
            elif is_date_expired == True:
                search_result_type = '2'
            else:
                search_result_type = '1'
            
            #store/update db row
            try:
                request_report_obj = RequestReport.objects.get(crash_report_num=cr_number)
            except RequestReport.DoesNotExist:
                request_report_obj = RequestReport()
                request_report_obj.inserted_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            request_report_obj.crash_report_num = cr_number
            request_report_obj.driver_name = driver_name
            request_report_obj.crash_date = datetime.strptime(cr_date, "%m/%d/%Y").strftime('%Y-%m-%d')
            request_report_obj.county = results[0]['County']
            request_report_obj.search_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            request_report_obj.search_result = search_result_type
            request_report_obj.updatd_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            
            request_report_obj.save()
        else:
            search_result_type == '0'
            try:
                request_report_obj = RequestReport.objects.get(crash_report_num=cr_number)
            except RequestReport.DoesNotExist:
                request_report_obj = RequestReport()
                request_report_obj.inserted_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            request_report_obj.crash_report_num = cr_number
            request_report_obj.search_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            request_report_obj.search_result = search_result_type
            request_report_obj.updatd_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            
            request_report_obj.save()

        return redirect('request-report')
def nu(num1, num2):
    digits = len(str(num2))
    num1 = num1 * (10 ** digits)
    num1 += num2
    return num1

def split(word): 
    return [char for char in word] 

def parse_pdf(request):
    if request.method == "POST":
        file_attached = request.FILES["filename"]
        data = scrap_data(request.FILES["filename"])
        month = int(data.get("Date_Month"))
        day = int(data.get("Date_Day"))
        year = int(data.get("Date_year"))
        data_date = datetime.strptime(str(nu(year, nu(day, month))), "%Y%d%m")
        dob_date= data.get("DOB_Month") + str("/")+data.get("DOB_Day") +str("/")+ data.get("DOB_Year")
        inputt = data.get('telephone')
        dt = split(inputt)
        telephone1 = str("""(""") + str(dt[0]) + str(dt[1]) +str(dt[2])+  str(""")""") +str(dt[3]) + str(dt[4])+str(dt[5]) + str("""-""") + str(dt[6]) + str(dt[7])+ str(dt[8])+ str(dt[9])

        bc = data["Drivers_full_name_Street_Address_City_and_State"].split(" ")
        name= []
        add =[]
        y= 'sdf'
        for x in bc:
           try:
            int(x)
            add.append(str(x))
            y = "fds"
           except Exception as e:
                 if y =='sdf':
                   name.append(x)
                 else:
                   add.append(x)
                   dfname = ' '.join(map(str,name))
                   daddess = ' '.join(map(str,add))

        pk = CrashReport.objects.create(
            crash_report_case_no=data["crash_report_case_no"],
            local_case_no=data["local_case_no"],
            date=data_date,
            time=data["time"],
            day_of_week=data["day_of_week"],
            county=data["county"],
            city=data["city"],
            Drivers_full_name=dfname,
            Street_Address_City_and_State=daddess,
            zipcode=data["zipcode"],
            telephone=telephone1,
            dob=dob_date,
            race=data["race"],
            sex=data["sex"],
            dL_state=data["dL_state"],
            driving_license_no=data["driving_license_no"],
            file_attached=file_attached,
        )
        messages.success(request, f"Scraped and saved successfully!")
        return redirect("car-report")
    return render(request, "data_report.html")

def savefile(request):

        form = CarReportForm(request.POST)
        if form.is_valid():
            form.save()
        queryset = CrashReport.objects.all()
        queryset = {"queryset": queryset}

        return render(request, "uploadedpdf.html", queryset)


def requestreportview(request):

    return render(request, "Request_report.html", {})

def automator(request):
    if request.method == "POST":
        pass

