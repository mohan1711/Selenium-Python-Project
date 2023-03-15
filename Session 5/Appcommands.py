import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get('https://www.saucedemo.com/')
time.sleep(5)
print(driver.title)     #Swag Labs
print(driver.current_url)       #https://www.saucedemo.com/
time.sleep(2)
driver.close()