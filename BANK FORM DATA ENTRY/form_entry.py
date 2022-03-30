# import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import xlrd 

excel_loc = 'Disk Name:<path>\\data_source.xls'
wb = xlrd.open_workbook(excel_loc)
sheet = wb.sheet_by_index(0)

# Total data (from data_source.xls)
start = 1
total = 530

# Worker Code 
eventYMMM = ''
eventDD = ''
eventXXXX = ''
segment = ''
referal = '' 

# Create webdriver object
driver = webdriver.Chrome()

# HSBC form elements
for i in range(start, total+1 ):
    driver.get("https://www.hsbc.co.id/1/2/WAB/leads-capturing?WABFormEntryCommand=cmd_init&hidden_fields.source=ThankyouPage&hidden_fields.campaign=leads")
    print(f'Data Queue: {i} from {total}')
    
    element_1 = driver.find_element_by_id("input-eventYMMM")
    element_1.send_keys(eventYMMM)
    element_2 = driver.find_element_by_id("input-eventDD")
    element_2.send_keys(eventDD)
    element_3 = driver.find_element_by_id("input-eventXXXX")
    element_3.send_keys(eventXXXX)

        
    element_nama = driver.find_element_by_id("input-name")
    element_nama.send_keys(sheet.cell_value(i, 0))

    element_no_telp = driver.find_element_by_id("input-phone")
    element_no_telp.send_keys(sheet.cell_value(i, 1))

    element_segment = Select(driver.find_element_by_id("input-selectsegment"))
    element_segment.select_by_value(segment)

    element_aoc = driver.find_element_by_id("input-aoc")
    element_aoc.send_keys(referal)

    element_cb = driver.find_element_by_class_name('checkmark').click()
    element_submit = driver.find_element_by_xpath('.//div[input/@id="submitButton"]').click()
    

driver.close()