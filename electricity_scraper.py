# reference: https://www.selenium.dev/documentation/webdriver/getting_started/first_script/ 
# set to anaconda kernel (this does not work with all interpreters, not sure why)

from selenium import webdriver
#from selenium.webdriver.chrome.options import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#from selenium.support.ui.select import Select
import time
import os

driver = webdriver.Chrome()

# TODO: add an array of buildings instead to allow multiple
building = "ToniMorrisonHall"

driver.get("https://portal.emcs.cornell.edu/dashboard/script/portal.js?orgId=2&var-portal_group=ToniMorrisonHall")
# ask chatgpt about conversion
#driver.get("https://portal.emcs.cornell.edu/dashboard/script/portal.js?orgId=2&var-portal_group=ToniMorrisonHall")

driver.implicitly_wait(60)

time_button = driver.find_element(by=By.XPATH, value='//button[@aria-label="Time range picker with current time range Last 24 hours selected"]')
data_type_button = driver.find_element(by = By.XPATH, value='//select[@name="slottype"]')
download_button = driver.find_element(by = By.XPATH, value='//button[@class="btn btn-success"]')

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
start_year = 2023
end_year = 2023
start_month = 1
end_month = 3

# Change based on your computer/file path
former_filepath = "/Users/lillianhwang-geddes/Downloads/"
new_folder_path = "/Users/lillianhwang-geddes/Documents/College/Geodata/CornellElecMap/ScrapedFiles"

for yr in range(start_year, end_year+1):
  for mth in range(start_month, end_month+1):
    for i in range(0, 2):

      # download data file
      time_button.click()
      start_time = driver.find_element(by = By.XPATH, value='//input[@aria-label="Time Range from field"]')
      end_time = driver.find_element(by = By.XPATH, value='//input[@aria-label="Time Range to field"]')
      apply_button = driver.find_element(by = By.XPATH, value='//button[@class="css-1sara2j-button"]')
      #time_button.click()

      if mth < 10:
        m = "0" + str(mth)
      else:
        m = str(mth)

      if i == 0:
        start_day = '01'
        end_day = '15'
      else:
        start_day = '16'
        end_day = str(days_in_month[mth-1])
        if yr % 4 == 0 and mth == 2:
          end_day = '29' # leap day

      start_time.clear()
      start_time.send_keys(str(yr) + '-' + m + '-' + start_day + ' 00:00:00')

      end_time.clear()
      end_time.send_keys(str(yr) + '-' + m + '-' + end_day + ' 23:59:59')

      apply_button.click() 

      select_data = Select(data_type_button)
      select_data.select_by_visible_text("No aggregation (raw data)")

      download_button.click()

      # rename data file and put it in correct folder

      # TODO: fix this part, there are some issues
      os.rename(former_filepath+"Exported Data.xlsx", new_folder_path+"/"+building+str(yr)+"-"+str(mth)+"-"+str(i)+".xlsx")

      driver.implicitly_wait(60)