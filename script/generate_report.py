from selenium import webdriver
from time import sleep


SECOND_ADDRESS = "SECOND_ADDRESS"
CITY = "CITY"
FIRSTNAME = "FIRSTNAME"
LASTNAME = "LASTNAME"
PHONENUMBER = "123-123-1234"
CRASHREPORTNUMBER = "0699958"
CCNUMBER = "1234567891234567"
CCNAME = "CCNAME"
CCADDRESS1 = "CCADDRESS1"
CCZIP = "55555-4444"


driver = webdriver.Chrome(
    executable_path="C:/Users/me/Downloads/driver/chromedriver.exe"
)
driver.get("https://www.alabamainteractive.org/dps_crash_report")

driver.find_element_by_id("mainMenu_mainMenuObject_confirmation").click()

driver.find_element_by_xpath("//input[@value='Purchase Crash Report']").click()


inputElement = driver.find_element_by_xpath(
    "//input[@name='contactInformationObject.firstName']"
)
inputElement.send_keys(FIRSTNAME)

inputElement = driver.find_element_by_xpath(
    "//input[@name='contactInformationObject.lastName']"
)
inputElement.send_keys(LASTNAME)

inputElement = driver.find_element_by_xpath(
    "//input[@name='contactInformationObject.phoneNumber']"
)
inputElement.send_keys(PHONENUMBER)

driver.find_element_by_xpath("//input[@value='Continue']").click()

inputElement = driver.find_element_by_xpath(
    "//input[@name='crashReportSearchObject.crashReportNumber']"
)
inputElement.send_keys(CRASHREPORTNUMBER)

driver.find_element_by_xpath("//input[@value='Search for Report']").click()

sleep(3)

driver.find_element_by_link_text("Add to Cart").click()

sleep(10)

inputElement = driver.find_element_by_xpath(
    "//input[@name='crashReportSearchObject.crashReportNumber']"
)
inputElement.send_keys("CRASHREPORTNUMBER")

driver.find_element_by_xpath("//input[@value='Search for Report']").click()

sleep(3)

driver.find_element_by_link_text("Add to Cart").click()

sleep(10)

driver.find_element_by_xpath("//input[@value='Proceed to Cart']").click()

driver.find_element_by_id("summary_summaryObject_confirmation").click()

sleep(3)

driver.find_element_by_xpath("//input[@value='Checkout']").click()

driver.find_element_by_xpath(
    "//select[@name='creditCardObject.cctype']/option[text()='Visa']"
).click()

inputElement = driver.find_element_by_xpath(
    "//input[@name='creditCardObject.ccnumber']"
)
inputElement.send_keys(CCNUMBER)

driver.find_element_by_xpath(
    "//select[@name='creditCardObject.ccexprmonth']/option[text()='Jan (01)']"
).click()
driver.find_element_by_xpath(
    "//select[@name='creditCardObject.ccexpryear']/option[text()='2020']"
).click()

inputElement = driver.find_element_by_xpath("//input[@name='creditCardObject.ccname']")
inputElement.send_keys(CCNAME)

inputElement = driver.find_element_by_xpath(
    "//input[@name='creditCardObject.ccaddress1']"
)
inputElement.send_keys(CCADDRESS1)

inputElement = driver.find_element_by_xpath(
    "//input[@name='creditCardObject.ccaddress2']"
)
inputElement.send_keys(SECOND_ADDRESS)

inputElement = driver.find_element_by_xpath("//input[@name='creditCardObject.cccity']")
inputElement.send_keys(CITY)

driver.find_element_by_xpath(
    "//select[@name='creditCardObject.ccstate']/option[text()='Alabama']"
).click()

inputElement = driver.find_element_by_xpath("//input[@name='creditCardObject.cczip']")
inputElement.send_keys(CCZIP)

driver.find_element_by_xpath("//input[@value='Submit Payment']").click()
