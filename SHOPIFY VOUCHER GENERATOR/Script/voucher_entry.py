# import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import xlrd 

excel_loc = '<path>\\Spreadsheet\\data_code_vouc.xls'

wb = xlrd.open_workbook(excel_loc)
sheet = wb.sheet_by_index(0)

# create webdriver object
options = Options()

# No need to login again
options.add_argument('user-data-dir=C:\\Users\\<PCusername>\\AppData\\Local\\Google\\Chrome\\User Data')

driver = webdriver.Chrome(options=options)

# Total entries
start = 1
total = 1007

# Value field

limit = '1'
date_1 = '2022-01-25'
time_1 = '12:00 AM'
date_2 = '2022-07-31'
time_2 = '11:59 PM'

def start_app():
    for i in range(start, total+1 ):
            
        driver.get("https://sepasang-collection.myshopify.com/admin/discounts/new")
        print(f'Kode ke: {i} dari {total}')

        element_disc_code = driver.find_element_by_id('PolarisTextField1')
        element_disc_code.send_keys(sheet.cell_value(i, 0))

        element_types = driver.find_element_by_css_selector("#PolarisChoiceList1 > ul:nth-child(2) > li:nth-child(2) > label:nth-child(1) > span:nth-child(2)")
        element_types.click()

        element_value = driver.find_element_by_id('fixedAmountValueField')
        element_value.send_keys(str(sheet.cell_value(i, 1)))

        element_usage = driver.find_element_by_css_selector("#PolarisChoiceList5\[\] > ul:nth-child(2) > li:nth-child(1) > label:nth-child(1)")
        element_usage.click()

        element_usage_limit = driver.find_element_by_id('totalUsageLimit')
        element_usage_limit.send_keys(limit)

        element_active_dates_1 = driver.find_element_by_id("StartEmbeddedDatePicker")
        element_active_dates_1.send_keys(Keys.CONTROL, "a"); 
        element_active_dates_1.send_keys(Keys.DELETE)
        element_active_dates_1.send_keys(date_1)

        element_active_time_1 = driver.find_element_by_id("StartTimeField")
        element_active_time_1.send_keys(Keys.CONTROL, "a"); 
        element_active_time_1.send_keys(Keys.DELETE)
        element_active_time_1.send_keys(time_1)

        element_end_date = driver.find_element_by_css_selector('div.Polaris-FormLayout--grouped_17srt:nth-child(2) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > span:nth-child(1) > span:nth-child(1) > span:nth-child(2)').click()

        element_active_dates_2 = driver.find_element_by_id("EndEmbeddedDatePicker")
        element_active_dates_2.send_keys(Keys.CONTROL, "a"); 
        element_active_dates_2.send_keys(Keys.DELETE)
        element_active_dates_2.send_keys(date_2)

        element_active_time_2 = driver.find_element_by_id("EndTimeField")
        element_active_time_2.send_keys(Keys.CONTROL, "a"); 
        element_active_time_2.send_keys(Keys.DELETE)
        element_active_time_2.send_keys(time_2)

        # element_submit = driver.find_element_by_css_selector('#AppFrameMain > div > div > div.Polaris-Page__Content_xd1mk > div > div:nth-child(3) > div > div > div:nth-child(2) > button > span > span').click()
        
    driver.close()
try:
    start_app()
except TimeoutException as ex:
    driver.refresh()
    start_app()