from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

def request_report():

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


    # Define Chrome options to open the window in maximized mode
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # Initialize the Chrome webdriver and open the URL
    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(30)

    # driver = webdriver.Chrome(
    #     executable_path="C:/Users/me/Downloads/driver/chromedriver.exe"
    # )
    
    # Step 1: Confirm Agreement Page, https://www.alabamainteractive.org/dps_crash_report/contactInformation.action
    # Check the agree terms and Click the button 'Purchase Crash Report'
    driver.get("https://www.alabamainteractive.org/dps_crash_report")
    driver.find_element_by_id("mainMenu_mainMenuObject_confirmation").click()
    driver.find_element_by_xpath("//input[@value='Purchase Crash Report']").click()

    # Step 2: Contact Information Page, https://www.alabamainteractive.org/dps_crash_report/mainMenu.action
    # Enter FirstName, LastName, PhoneNumber, EmailAddres and then Click 'Continue' button
    inputElement = driver.find_element_by_xpath("//input[@name='contactInformationObject.firstName']")
    inputElement.send_keys(FIRSTNAME)

    inputElement = driver.find_element_by_xpath("//input[@name='contactInformationObject.lastName']")
    inputElement.send_keys(LASTNAME)

    inputElement = driver.find_element_by_xpath("//input[@name='contactInformationObject.phoneNumber']")
    inputElement.send_keys(PHONENUMBER)

    driver.find_element_by_xpath("//input[@value='Continue']").click()

    # Step 3: Crash Report Search Page, https://www.alabamainteractive.org/dps_crash_report/contactInformation.action
    # Enter the Crash Report Number and Click 'Search for Report' button
    inputElement = driver.find_element_by_xpath("//input[@name='crashReportSearchObject.crashReportNumber']")
    inputElement.send_keys(CRASHREPORTNUMBER)

    driver.find_element_by_xpath("//input[@value='Search for Report']").click()

    sleep(3)
    
    soup = BeautifulSoup(driver.page_source, "lxml")
    report = scrape_reportinfo(soup)

    # driver.find_element_by_link_text("Add to Cart").click()

    # sleep(10)

    # inputElement = driver.find_element_by_xpath(
    #     "//input[@name='crashReportSearchObject.crashReportNumber']"
    # )
    # inputElement.send_keys("CRASHREPORTNUMBER")

    # driver.find_element_by_xpath("//input[@value='Search for Report']").click()

    # sleep(3)

    # driver.find_element_by_link_text("Add to Cart").click()

    # sleep(10)

    # driver.find_element_by_xpath("//input[@value='Proceed to Cart']").click()

    # driver.find_element_by_id("summary_summaryObject_confirmation").click()

    # sleep(3)

    # driver.find_element_by_xpath("//input[@value='Checkout']").click()

    # driver.find_element_by_xpath(
    #     "//select[@name='creditCardObject.cctype']/option[text()='Visa']"
    # ).click()

    # inputElement = driver.find_element_by_xpath(
    #     "//input[@name='creditCardObject.ccnumber']"
    # )
    # inputElement.send_keys(CCNUMBER)

    # driver.find_element_by_xpath(
    #     "//select[@name='creditCardObject.ccexprmonth']/option[text()='Jan (01)']"
    # ).click()
    # driver.find_element_by_xpath(
    #     "//select[@name='creditCardObject.ccexpryear']/option[text()='2020']"
    # ).click()

    # inputElement = driver.find_element_by_xpath("//input[@name='creditCardObject.ccname']")
    # inputElement.send_keys(CCNAME)

    # inputElement = driver.find_element_by_xpath(
    #     "//input[@name='creditCardObject.ccaddress1']"
    # )
    # inputElement.send_keys(CCADDRESS1)

    # inputElement = driver.find_element_by_xpath(
    #     "//input[@name='creditCardObject.ccaddress2']"
    # )
    # inputElement.send_keys(SECOND_ADDRESS)

    # inputElement = driver.find_element_by_xpath("//input[@name='creditCardObject.cccity']")
    # inputElement.send_keys(CITY)

    # driver.find_element_by_xpath(
    #     "//select[@name='creditCardObject.ccstate']/option[text()='Alabama']"
    # ).click()

    # inputElement = driver.find_element_by_xpath("//input[@name='creditCardObject.cczip']")
    # inputElement.send_keys(CCZIP)

    # driver.find_element_by_xpath("//input[@value='Submit Payment']").click()

# To Get each letter page url link
def scrape_reportinfo(soup):

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

    print(reports)
    return reports
    
request_report()