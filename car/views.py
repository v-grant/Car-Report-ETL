import io
import os
from django.shortcuts import render, redirect
from .forms import CarReportForm, DataViewForm, RequestReportForm
from .models import CrashReport, RequestReport
from datetime import datetime
import datetime
from django.views.static import serve
from django.contrib import messages
from django.views.generic import View
from reportlab.pdfgen import canvas
from bs4 import BeautifulSoup
import pdfplumber
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

def scrap_data(file_data):

    pdf = pdfplumber.open(file_data)
    page = pdf.pages[0]
    crcn = page.extract_text()[66:73]
    dict1 = {}
    dict1 = {}
    for c1, table in enumerate(page.extract_tables()):
        for c2, list in enumerate(table):
            for c3, x in enumerate(list):
                if x != None:
                    d = {"crash_report_case_no": crcn}
                    dict1.update(d)
                    if c1 == 2 and c2 == 0 and c3 == 0:
                        d = {"local_case_no": x[15:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 3:
                        d = {"date_month": x}
                        dict1.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 4:
                        d = {"date_day": x}
                        dict1.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 8:
                        d = {"date_year": x}
                        dict1.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 13:
                        d = {"time": x[5:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 21:
                        d = {"day_of_week": x[12:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 26:
                        d = {"county": x[7:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 38:
                        d = {"city": x[11:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 7 and c3 == 2:
                        d = {"Drivers_full_name_Street_Address_City_and_State": x[47:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 7 and c3 == 46:
                        d = {"zipcode": x[4:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 7 and c3 == 50:
                        d = {"telephone": x[10:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 8 and c3 == 3:
                        d = {"DOB_Month": x}
                        dict1.update(d)
                    if c1 == 0 and c2 == 8 and c3 == 4:
                        d = {"DOB_Day": x}
                        dict1.update(d)
                    if c1 == 0 and c2 == 8 and c3 == 8:
                        d = {"DOB_Year": x}
                        dict1.update(d)
                    if c1 == 0 and c2 == 8 and c3 == 12:
                        d = {"race": x[5:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 8 and c3 == 15:
                        d = {"sex": x[4:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 8 and c3 == 16:
                        d = {"dL_state": x[9:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 8 and c3 == 20:
                        d = {"driving_license_no": x[19:]}
                        dict1.update(d)
                        d = {"crash_report_case_no": crcn}
                    dict1.update(d)
                    if c1 == 2 and c2 == 0 and c3 == 0:
                        d = {"local_case_no": x[15:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 3:
                        d = {"date_month1": x}
                        dict1.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 4:
                        d = {"date_day1": x}
                        dict1.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 8:
                        d = {"date_year1": x}
                        dict1.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 13:
                        d = {"time1": x[5:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 21:
                        d = {"day_of_week1": x[12:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 26:
                        d = {"county1": x[7:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 38:
                        d = {"city1": x[11:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 24 and c3 == 2:
                        d = {"Drivers_full_name_Street_Address_City_and_State1": x[47:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 24 and c3 == 46:
                        d = {"zipcode1": x[4:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 24 and c3 == 50:
                        d = {"telephone1": x[10:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 25 and c3 == 3:
                        d = {"DOB_Month1": x}
                        dict1.update(d)
                    if c1 == 0 and c2 == 25 and c3 == 4:
                        d = {"DOB_Day1": x}
                        dict1.update(d)
                    if c1 == 0 and c2 == 25 and c3 == 8:
                        d = {"DOB_Year1": x}
                        dict1.update(d)
                    if c1 == 0 and c2 == 25 and c3 == 12:
                        d = {"race1": x[5:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 25 and c3 == 15:
                        d = {"sex1": x[4:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 25 and c3 == 16:
                        d = {"dL_state1": x[9:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 25 and c3 == 20:
                        d = {"driving_license_no1": x[19:]}
                        dict1.update(d)
    return dict1


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
        month = int(data.get("date_month"))
        day = int(data.get("date_day"))
        year = int(data.get("date_year"))
        data_date = datetime.datetime.strptime(str(nu(year, nu(day, month))), "%Y%d%m")
        dob_date= data.get("DOB_Month") + str("/")+data.get("DOB_Day") +str("/")+ data.get("DOB_Year")
        inputt = data.get('telephone')
        dt = split(inputt)
        telephone1 = str("""(""") + str(dt[0]) + str(dt[1]) +str(dt[2])+ str(""")""") +str(dt[3]) + str(dt[4])+str(dt[5]) + str("""-""") + str(dt[6]) + str(dt[7])+ str(dt[8])+ str(dt[9])
        bc = data["Drivers_full_name_Street_Address_City_and_State"].split(" ")
    
        # for second driver
        month1 = int(data.get("date_month1"))
        day1 = int(data.get("date_day1"))
        year1 = int(data.get("date_year1"))
        data_date1 = datetime.datetime.strptime(str(nu(year1, nu(day1, month1))), "%Y%d%m")
        dob_date1= data.get("DOB_Month1") + str("/")+data.get("DOB_Day1") +str("/")+ data.get("DOB_Year1")
        inputt1 = data.get('telephone1')
        dt1 = split(inputt1)
        telephone2 = str("""(""") + str(dt1[0]) + str(dt1[1]) +str(dt1[2])+  str(""")""") +str(dt1[3]) + str(dt1[4])+str(dt1[5]) + str("""-""") + str(dt1[6]) + str(dt1[7])+ str(dt1[8])+ str(dt1[9])
        bc1 = data["Drivers_full_name_Street_Address_City_and_State1"].split(" ")
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
        name1= []
        add1 =[]
        y1= 'sdf'
        for x1 in bc1:
           try:
            int(x1)
            add1.append(str(x1))
            y1 = "fds"
           except Exception as e:
                 if y1 =='sdf':
                   name1.append(x1)
                 else:
                   add1.append(x1)
                   dfname1 = ' '.join(map(str,name1))
                   daddess1 = ' '.join(map(str,add1)) 
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

        """
        Code commmented for the 2nd driver info saving
        """
        # pk = CrashReport.objects.create(
        #     crash_report_case_no=data["crash_report_case_no"],
        #     local_case_no=data["local_case_no"],
        #     date=data_date1,
        #     time=data["time1"],
        #     day_of_week=data["day_of_week1"],
        #     county=data["county1"],
        #     city=data["city1"],
        #     Drivers_full_name=dfname1,
        #     Street_Address_City_and_State=daddess1,
        #     zipcode=data["zipcode1"],
        #     telephone=telephone2,
        #     dob=dob_date1,
        #     race=data["race1"],
        #     sex=data["sex1"],
        #     dL_state=data["dL_state1"],
        #     driving_license_no=data["driving_license_no1"],
        #     file_attached=file_attached,
        # )
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
    return render(request, "Request_report.html", {'report_data': RequestReport.objects.all()})

def automator(request):
    if request.method == "POST":
        pass

def mcrequest_report(request, *args, **kwargs):
  if request.method == 'POST':
    
    SECOND_ADDRESS = "SECOND_ADDRESS"
    CITY = "CITY"
    FIRSTNAME = "FIRSTNAME"
    LASTNAME = "LASTNAME"
    PHONENUMBER = "123-123-1234"
    CRASHREPORTNUMBER = "0707261"
    CCNUMBER = "1234567891234567"
    CCNAME = "CCNAME"
    CCADDRESS1 = "CCADDRESS1"
    CCZIP = "55555-4444"

    # chrome_options=options()
    # chrome_options.add_argument('--headless')
    # Define Chrome options to open the window in maximized mode
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # Initialize the Chrome webdriver and open the URL
    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(30)

    # driver = webdriver.Chrome(
    #     executable_path="C:/Users/me/Downloads/driver/chromedriver.exe"
    # )
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
    
    #for searching data in range between
    
    # for number in range(707261, 707501):
    #     num = "0"+str(number)

    inputElement = driver.find_element_by_xpath("//input[@name='crashReportSearchObject.crashReportNumber']")
    inputElement.send_keys(CRASHREPORTNUMBER)

    driver.find_element_by_xpath("//input[@value='Search for Report']").click()
    sleep(3)
        # try:
    driver.find_element_by_link_text("Add to Cart").click()
    sleep(10)
        # except:
    inputElement = driver.find_element_by_xpath("//input[@name='crashReportSearchObject.crashReportNumber']") # .clear()
        


    soup = BeautifulSoup(driver.page_source, "lxml")
        # data = {"report_number":CRASHREPORTNUMBER, "soup_output":soup}
    report = scrape_reportinfo(soup, CRASHREPORTNUMBER)

    return render(request, "Request_Report.html" , {'data': report})
  
  return render(request, "Request_Report.html" , {'datar': 'No data fetched'})

# To Get each letter page url link
def scrape_reportinfo(soup, CRASHREPORTNUMBER):

    reports = []

    container = soup.find('form', {"id": "crash-search-form"})
    table = container.find_all('table')[-1]
    print(table)
    print(table.find('td', {"class": "reportHeader"}))
    # if table.find('td', {"class": "reportHeader"}) is not None and table.find('td', {"class": "reportHeader"}).text.strip() == "Search Results":
    index = 1
    for inner_tr in table.tbody.find_all('tr', recursive=False):
        print(inner_tr)
        if index < 3: 
            index = index + 1
            continue
        reports.append({'Crash_Date': inner_tr.find_all('td')[0].text.strip(), 'Name': inner_tr.find_all('td')[1].text.strip(), 'County': inner_tr.find_all('td')[2].text.strip()})
    post_values ={}
    for x in reports:
        post_values['driver_name'] =x.get("Name").replace(",", "")
        post_values['crash_date'] =x.get("Crash_Date")
        post_values['county'] =x.get("County")  
        post_values['crash_report_num']= CRASHREPORTNUMBER
        form = RequestReportForm(post_values)
        if form.is_valid():
            form.save()
    pd= []
    for x in reports:
        for key, value in x.items():
         m=value.replace(',','')
         n=key
         pd.append("{"+n+':'+m+"}")
    # print(reports)
    return reports
# request_report()
