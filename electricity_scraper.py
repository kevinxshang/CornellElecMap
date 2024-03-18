# reference: https://www.selenium.dev/documentation/webdriver/getting_started/first_script/ 

from selenium import webdriver
#from selenium.webdriver.chrome.options import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#from selenium.support.ui.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://portal.emcs.cornell.edu/dashboard/script/portal.js?orgId=2&var-portal_group=ToniMorrisonHall&kiosk=tv&from=1676523600000&to=1677646799000")

driver.implicitly_wait(.5)

# todo: fix this, find right label to use
time_button = driver.find_element(by=By.XPATH, value='//button[@class="toolbar-button css-fbg4cg-toolbar-button"]')
time_button.click()

start_time = driver.find_element(by = By.XPATH, value='//input[@aria-label="Time Range from field"]')
start_time.send_keys('2023-03-16 00:00:00')

end_time = driver.find_element(by = By.XPATH, value='//input[@aria-label="Time Range to field"]')
start_time.send_keys('2023-03-31 23:59:59')

apply_button = driver.find_element(by = By.XPATH, value='//button[@class="css-1sara2j-button"]')
apply_button.click()

# todo: choose raw data
data_type_button = driver.find_element(by = By.XPATH, value='//select[@name="slottype"]')
select_data = Select(data_type_button)
select_data.select_by_visible_text("No aggregation (raw data)")

download_button = driver.find_element(by = By.XPATH, value='//button[@class="btn btn-success"]')
download_button.click()

driver.implicitly_wait(5)

# todo: choose the right timeframes and download raw data
# need to figure out how to write in a text box in order to type in dates