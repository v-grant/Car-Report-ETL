import pdfplumber
import os

def scrap_data(file_data):

    pdf = pdfplumber.open(file_data)
    page = pdf.pages[0]
    crcn = page.extract_text()[66:73]
    dict1 = {}
    d = {"crash_report_case_no": crcn}
    dict1.update(d)
    drivers = []
    #temporary
    driver1 = {}
    driver2 = {}
    for c1, table in enumerate(page.extract_tables()):
        for c2, list in enumerate(table):
            for c3, x in enumerate(list):
                if x != None:                
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
                        driver1.update(d)
                    if c1 == 0 and c2 == 7 and c3 == 46:
                        d = {"zipcode": x[4:]}
                        driver1.update(d)
                    if c1 == 0 and c2 == 7 and c3 == 50:
                        d = {"telephone": x[10:]}
                        driver1.update(d)
                    if c1 == 0 and c2 == 8 and c3 == 3:
                        d = {"DOB_Month": x}
                        driver1.update(d)
                    if c1 == 0 and c2 == 8 and c3 == 4:
                        d = {"DOB_Day": x}
                        driver1.update(d)
                    if c1 == 0 and c2 == 8 and c3 == 8:
                        d = {"DOB_Year": x}
                        driver1.update(d)
                    if c1 == 0 and c2 == 8 and c3 == 12:
                        d = {"race": x[5:]}
                        driver1.update(d)
                    if c1 == 0 and c2 == 8 and c3 == 15:
                        d = {"sex": x[4:]}
                        driver1.update(d)
                    if c1 == 0 and c2 == 8 and c3 == 16:
                        d = {"dL_state": x[9:]}
                        driver1.update(d)
                    if c1 == 0 and c2 == 8 and c3 == 20:
                        d = {"driving_license_no": x[19:]}
                        driver1.update(d)
                    if c1 == 0 and c2 == 24 and c3 == 2:
                        d = {"Drivers_full_name_Street_Address_City_and_State": x[47:]}
                        driver2.update(d)
                    if c1 == 0 and c2 == 24 and c3 == 46:
                        d = {"zipcode": x[4:]}
                        driver2.update(d)
                    if c1 == 0 and c2 == 24 and c3 == 50:
                        d = {"telephone": x[10:]}
                        driver2.update(d)
                    if c1 == 0 and c2 == 25 and c3 == 3:
                        d = {"DOB_Month": x}
                        driver2.update(d)
                    if c1 == 0 and c2 == 25 and c3 == 4:
                        d = {"DOB_Day": x}
                        driver2.update(d)
                    if c1 == 0 and c2 == 25 and c3 == 8:
                        d = {"DOB_Year": x}
                        driver2.update(d)
                    if c1 == 0 and c2 == 25 and c3 == 12:
                        d = {"race": x[5:]}
                        driver2.update(d)
                    if c1 == 0 and c2 == 25 and c3 == 15:
                        d = {"sex": x[4:]}
                        driver2.update(d)
                    if c1 == 0 and c2 == 25 and c3 == 16:
                        d = {"dL_state": x[9:]}
                        driver2.update(d)
                    if c1 == 0 and c2 == 25 and c3 == 20:
                        d = {"driving_license_no": x[19:]}
                        driver2.update(d)
    drivers.append(driver1)
    drivers.append(driver2)
    d = {'drivers': drivers}
    dict1.update(d)
    return dict1