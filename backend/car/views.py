import io
from django.shortcuts import render, redirect
from .forms import CarReportForm, DataViewForm, RequestReportForm
from .models import CrashReport
from datetime import datetime
import datetime
from django.views.static import serve
from django.contrib import messages
from django.views.generic import View
from reportlab.pdfgen import canvas
import pdfplumber
import reportlab
from selenium import webdriver
from time import sleep

class CrashReportViews(View):
    def get(self, request, *args, **kwargs):
        queryset = CrashReport.objects.all()
        queryset = {"queryset": queryset}
        # import pdb; pdb.set_trace()
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
        file_attached = request.FILES["filename"]
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

def savefile(request):

        form = CarReportForm(request.POST)
        if form.is_valid():
            form.save()
        queryset = CrashReport.objects.all()
        queryset = {"queryset": queryset}

        return render(request, "uploadedpdf.html", queryset)


def requestreportview(request):
        form = RequestReportForm(request.POST)
        if form.is_valid():
            form.save()

            SECOND_ADDRESS = "SECOND_ADDRESS"
            CITY = "CITY"
            FIRSTNAME="FIRSTNAME"
            LASTNAME= "LASTNAME"
            PHONENUMBER = '123-123-1234' 
            CRASHREPORTNUMBER = '0699958'
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

            driver.find_element_by_xpath("//input[@value='Search for Report']").click()

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
            return render(request, "Request_report.html", {})
        return render(request, "Request_report.html")
