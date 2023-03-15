import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get('https://www.saucedemo.com/')
time.sleep(2)
driver.get('https://demo.guru99.com/')
time.sleep(2)

driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)

driver.quit()