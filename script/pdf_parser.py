import pdfplumber
import os

def scrap_data(file_data):
    pdf = pdfplumber.open(file_data)
    

    # page = pdf.pages[0]
    pages = pdf.pages
    
    crcn = pages[0].extract_text()[66:73]
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

                    if c1 == 0 and c2 == 0 and c3 == 3:
                        d = {"date_month2": x}
                        dict1.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 4:
                        d = {"date_day2": x}
                        dict1.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 8:
                        d = {"date_year2": x}
                        dict1.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 13:
                        d = {"time2": x[5:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 21:
                        d = {"day_of_week2": x[12:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 26:
                        d = {"county2": x[7:]}
                        dict1.update(d)
                    if c1 == 0 and c2 == 0 and c3 == 38:
                        d = {"city2": x[11:]}
                        dict1.update(d)
                  
    

    for c1, table in enumerate(pages[1].extract_tables()):
        for c2, list in enumerate(table):
            for c3, x in enumerate(list):
                if x != None:
                    # print(f"{c1},{c2},{c3}-->{x}")                

                    if (c1 == 0 and c2 == 0 and c3 == 3):
                        d = {"Drivers_full_name_Street_Address_City_and_State2": x[47:]}
                        dict1.update(d)
                    if (c1 == 0 and c2 == 0 and c3 == 40):
                        d = {"zipcode2": x[4:]}
                        dict1.update(d)
                    if (c1 == 0 and c2 == 0 and c3 == 42):
                        d = {"telephone2": x[10:]}
                        dict1.update(d)
                    if (c1 == 0 and c2 == 1 and c3 == 4):
                        d = {"DOB_Month2": x}
                        dict1.update(d)
                    if (c1 == 0 and c2 == 1 and c3 == 6):
                        d = {"DOB_Day2": x}
                        dict1.update(d)
                    if (c1 == 0 and c2 == 1 and c3 == 9):
                        d = {"DOB_Year2": x}
                        dict1.update(d)
                    if (c1 == 0 and c2 == 1 and c3 == 13):
                        d = {"race2": x[5:]}
                        dict1.update(d)
                    if (c1 == 0 and c2 == 1 and c3 == 16):
                        d = {"sex2": x[4:]}
                        dict1.update(d)
                    if (c1 == 0 and c2 == 1 and c3 == 18):
                        d = {"dL_state2": x[9:]}
                        dict1.update(d)
                    if (c1 == 0 and c2 == 1 and c3 == 20):
                        d = {"driving_license_no2": x[19:]}
                        dict1.update(d)
    return dict1