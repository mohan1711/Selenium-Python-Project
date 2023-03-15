
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()

countries_all = driver.find_elements(By.XPATH,"//ul[contains(@id,'select2-billing_country-results')]//li")
# print(len(countries_all))       #249

for country in countries_all:
    if country.text == "India":
        country.click()
        break

time.sleep(10)