import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get('https://www.saucedemo.com/')
time.sleep(5)

element = driver.find_element(By.XPATH,"//input[@id='login-button']")
print(element.text)
print(element.get_attribute('name'))    #login-button