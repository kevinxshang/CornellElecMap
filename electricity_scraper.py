# reference: https://www.selenium.dev/documentation/webdriver/getting_started/first_script/ 
# set to anaconda kernel (this does not work with all interpreters, not sure why)

from selenium import webdriver
#from selenium.webdriver.chrome.options import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#from selenium.support.ui.select import Select
import time

driver = webdriver.Chrome()


driver.get("https://portal.emcs.cornell.edu/dashboard/script/portal.js?orgId=2&var-portal_group=ToniMorrisonHall")
# ask chatgpt about conversion
#driver.get("https://portal.emcs.cornell.edu/dashboard/script/portal.js?orgId=2&var-portal_group=ToniMorrisonHall")

driver.implicitly_wait(60)

time_button = driver.find_element(by=By.XPATH, value='//button[@aria-label="Time range picker with current time range Last 24 hours selected"]')
#time_button = driver.find_element(by=By.XPATH, value='//button[@testid="data-testid TimePicker Open Button"]')
time_button.click()
#time_button.click()

# Note - need to fix this part, maybe wait a bit until downloading? apply button may not work

start_time = driver.find_element(by = By.XPATH, value='//input[@aria-label="Time Range from field"]')
start_time.clear()
start_time.send_keys('2023-03-16 00:00:00')

driver.implicitly_wait(60)

end_time = driver.find_element(by = By.XPATH, value='//input[@aria-label="Time Range to field"]')
end_time.clear()
end_time.send_keys('2023-03-31 23:59:59')

driver.implicitly_wait(60)

apply_button = driver.find_element(by = By.XPATH, value='//button[@class="css-1sara2j-button"]')
apply_button.click() 

driver.implicitly_wait(60)

# todo: choose raw data
data_type_button = driver.find_element(by = By.XPATH, value='//select[@name="slottype"]')
select_data = Select(data_type_button)
select_data.select_by_visible_text("No aggregation (raw data)")

download_button = driver.find_element(by = By.XPATH, value='//button[@class="btn btn-success"]')
download_button.click()
download_button.click()

driver.implicitly_wait(60)

# todo: choose the right timeframes and download raw data
# need to figure out how to write in a text box in order to type in dates