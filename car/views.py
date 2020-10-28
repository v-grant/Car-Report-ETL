import io
from django.shortcuts import render, redirect
from .forms import CarReportForm, DataViewForm, RequestReportForm
from .models import CrashReport, RequestReport
from datetime import datetime
import datetime
from django.views.static import serve
from django.contrib import messages
from django.views.generic import View
from reportlab.pdfgen import canvas

import reportlab
from selenium import webdriver
from time import sleep

from script.pdf_parser import scrap_data
from .models import RequestReport

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
        data_date = datetime.datetime.strptime(str(nu(year, nu(day, month))), "%Y%d%m")
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


# pk = RequestReport.objects.create(
#     crash_report_num= ,
#     crash_date= ,
#     driver_name= ,
#     county= ,
#     search_date= ,
#     search_result= ,
#     inserted_date= ,
#     updatd_date= ,
# )


        SECOND_ADDRESS = "SECOND_ADDRESS"
        CITY = "CITY"
        FIRSTNAME="FIRSTNAME"
        LASTNAME= "LASTNAME"        
        PHONENUMBER = '123-123-1234'
        CRASHREPORTNUMBER = '0707277'
        CCNUMBER = '1234567891234567'
        CCNAME= "CCNAME"
        CCADDRESS1= "CCADDRESS1"
        CCZIP = '55555-4444'
        # driver = webdriver.Chrome()
        driver = webdriver.Chrome(executable_path='C:/Users/me/Downloads/driver/chromedriver.exe')
        driver.get("https://www.alabamainteractive.org/dps_crash_report")
        driver.find_element_by_id("mainMenu_mainMenuObject_confirmation").click()

        driver.find_element_by_xpath("//input[@value='Purchase Crash Report']").click()


        inputElement = driver.find_element_by_xpath("//input[@name='contactInformationObject.firstName']")
        inputElement.send_keys(FIRSTNAME)

        inputElement = driver.find_element_by_xpath("//input[@name='contactInformationObject.lastName']")
        inputElement.send_keys(LASTNAME)

        inputElement = driver.find_element_by_xpath("//input[@name='contactInformationObject.phoneNumber']")
        inputElement.send_keys(PHONENUMBER)

        driver.find_element_by_xpath("//input[@value='Continue']").click()

        inputElement = driver.find_element_by_xpath("//input[@name='crashReportSearchObject.crashReportNumber']")
        inputElement.send_keys(CRASHREPORTNUMBER)

        driver.find_element_by_xpath("//input[@value='Search for Report']").click()

        sleep(3)

        driver.find_element_by_link_text("Add to Cart").click()

        sleep(10)

        inputElement = driver.find_element_by_xpath("//input[@name='crashReportSearchObject.crashReportNumber']")
        inputElement.send_keys('CRASHREPORTNUMBER')

        driver.find_element_by_xpath("//input[@value='selectarch for Report']").click()

        sleep(3)

        driver.find_element_by_link_text("Add to Cart").click()

        sleep(10)

        # driver.find_element_by_link_text("Proceed to Cart").click()
        driver.find_element_by_xpath("//input[@value='Proceed to Cart']").click()

        driver.find_element_by_id("summary_summaryObject_confirmation").click()

        sleep(3)

        driver.find_element_by_xpath("//input[@value='Checkout']").click()

        driver.find_element_by_xpath("//select[@name='creditCardObject.cctype']/option[text()='Visa']").click()

        inputElement = driver.find_element_by_xpath("//input[@name='creditCardObject.ccnumber']")
        inputElement.send_keys(CCNUMBER)

        driver.find_element_by_xpath("//select[@name='creditCardObject.ccexprmonth']/option[text()='Jan (01)']").click()
        driver.find_element_by_xpath("//select[@name='creditCardObject.ccexpryear']/option[text()='2020']").click()

        inputElement = driver.find_element_by_xpath("//input[@name='creditCardObject.ccname']")
        inputElement.send_keys(CCNAME)

        inputElement = driver.find_element_by_xpath("//input[@name='creditCardObject.ccaddress1']")
        inputElement.send_keys(CCADDRESS1)

        inputElement = driver.find_element_by_xpath("//input[@name='creditCardObject.ccaddress2']")
        inputElement.send_keys(SECOND_ADDRESS)

        inputElement = driver.find_element_by_xpath("//input[@name='creditCardObject.cccity']")
        inputElement.send_keys(CITY)

        driver.find_element_by_xpath("//select[@name='creditCardObject.ccstate']/option[text()='Alabama']").click()

        inputElement = driver.find_element_by_xpath("//input[@name='creditCardObject.cczip']")
        inputElement.send_keys(CCZIP)

        driver.find_element_by_xpath("//input[@value='Submit Payment']").click()

