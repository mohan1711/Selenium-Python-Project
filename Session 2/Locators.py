import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")

driver = webdriver.Chrome(service=serv_obj)
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()
time.sleep(5)

#Id locator
# driver.find_element(By.ID,'small-searchterms').send_keys('iphone 11')
#xpath locator
# driver.find_element(By.XPATH,"//button[@type='submit']").click()

#link text locator
# driver.find_element(By.LINK_TEXT,'Register').click()

#class name locator
sliders = driver.find_elements(By.CLASS_NAME,'nivo-imageLink')
print(len(sliders))

#tag name locator
links = driver.find_elements(By.TAG_NAME,'nivo-imageLink')
print(len(links))