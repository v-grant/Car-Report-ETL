import io
import os
from django.shortcuts import render, redirect
from .forms import CarReportForm, DataViewForm, RequestReportForm
from .models import CrashReport, RequestReport, CrashDrivers
from datetime import datetime
import time
from django.views.static import serve
from django.contrib import messages
from django.views.generic import View
from reportlab.pdfgen import canvas
from bs4 import BeautifulSoup
import reportlab
from django.db.models import Q

#parsing & scraping scripts
from script.pdf_parser import scrap_data
from script.generate_report import search_report, scrape_reportinfo

class CrashReportViews(View):
    def get(self, request, *args, **kwargs):
        queryset = CrashDrivers.objects.all().order_by('-crash_report_case_no')
        queryset = {"queryset": queryset}
        return render(request, "data_report.html", queryset)
    def post(self, request, *args, **kwargs):
        file_attached = request.FILES["filename"]
        data = scrap_data(request.FILES["filename"])
        month = int(data.get("date_month"))
        day = int(data.get("date_day"))
        year = int(data.get("date_year"))
        data_date = datetime.strptime(str(nu(year, nu(day, month))), "%Y%d%m")
        
        try:
            cr_obj = CrashReport.objects.get(crash_report_case_no=data['crash_report_case_no'])
        except CrashReport.DoesNotExist:
            cr_obj = CrashReport()
        cr_obj.crash_report_case_no = data["crash_report_case_no"]
        cr_obj.local_case_no = data["local_case_no"]
        cr_obj.date = data_date
        cr_obj.time = data["time"]
        cr_obj.day_of_week = data["day_of_week"]
        cr_obj.county = data["county"]
        cr_obj.city = data["city"]
        cr_obj.file_attached = file_attached
        
        cr_obj.save()

        CrashDrivers.objects.filter(crash_report_case_no=data['crash_report_case_no']).delete()
        for driver in data.get('drivers'):
            dob_date= driver["DOB_Month"] + str("/")+driver["DOB_Day"] +str("/")+ driver["DOB_Year"]
            inputt = driver['telephone'].replace(" ", "")
            telephone = inputt
            if inputt.startswith('('):
                telephone = inputt
            elif inputt.startswith('+1'):
                dt = split(inputt)
                telephone = str("""(""") + str(dt[2]) + str(dt[3]) +str(dt[4])+ str(""")""") +str(dt[5]) + str(dt[6])+str(dt[7]) + str("""-""") + str(dt[8]) + str(dt[9])+ str(dt[10])+ str(dt[11])
            else:
                dt = split(inputt)
                telephone = str("""(""") + str(dt[0]) + str(dt[1]) +str(dt[2])+ str(""")""") +str(dt[3]) + str(dt[4])+str(dt[5]) + str("""-""") + str(dt[6]) + str(dt[7])+ str(dt[8])+ str(dt[9])
            bc = driver["Drivers_full_name_Street_Address_City_and_State"].split(" ")
            name= []
            add =[]
            y= 'sdf'
            for x in bc:
                if hasNumbers(x):
                    add.append(x)
                    y = "fds"
                else:
                    if y =='sdf':
                        name.append(x)
                    else:
                        add.append(x)
            dfname = ' '.join(map(str,name))
            daddess = ' '.join(map(str,add))

            cd_pk = CrashDrivers.objects.create(
                crash_report_case_no = data["crash_report_case_no"],
                Drivers_full_name= dfname,
                Street_Address_City_and_State = daddess,
                zipcode= driver['zipcode'],
                telephone = telephone,
                dob = dob_date,
                race = driver['race'],
                sex = driver['sex'],
                dL_state = driver['dL_state'],
                driving_license_no = driver['driving_license_no']
            )
        return redirect('car-report')

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
        reports = RequestReport.objects.filter(search_result__in=['1', '2', '3', '4']).order_by('-crash_report_num')
        return render(request, "request_report.html", {"reports": reports})
    
    def post(self, request, *args, **kwargs):
        cr_number = request.POST.get('cr_number')
        #run selenium to fetch the crach report
        count = 0

        driver = search_report()

        for count in range(0, 1000):
            print(cr_number)
            driver, results = scrape_reportinfo(driver, cr_number)
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
                if((now_timestamp - cr_timestamp) > (6 * 3600 * 24)):
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

            cr_number = increment_report_num(cr_number)
        
        driver.close()
        return redirect('request-report')

class PurchasedReportView(View):
    def get(self, request, *args, **kwargs):
        reports = RequestReport.objects.filter(report_confirmation_num__isnull=False).order_by('-crash_report_num')
        return render(request, "purchase_report.html", {"reports": reports})
def increment_report_num(report_num):
    
    return "0" + str(int(report_num[1:])+1)

def nu(num1, num2):
    digits = len(str(num2))
    num1 = num1 * (10 ** digits)
    num1 += num2
    return num1
def split(word): 
    return [char for char in word] 

def savefile(request):
        form = CarReportForm(request.POST)
        if form.is_valid():
            form.save()
        queryset = CrashReport.objects.all()
        queryset = {"queryset": queryset}
        return render(request, "uploadedpdf.html", queryset)

def requestreportview(request):
    return render(request, "request_report.html", {})


def automator(request):
    if request.method == "POST":
        pass

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)