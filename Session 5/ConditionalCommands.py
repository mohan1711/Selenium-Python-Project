import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get('https://www.saucedemo.com/')
time.sleep(5)

username = driver.find_element(By.ID,'user-name')
print('Display status',username.is_displayed()) #True
print('Enabled status',username.is_enabled())   #True