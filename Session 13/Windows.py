
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.nopcommerce.com/en")
driver.switch_to.new_window('window')
driver.get("https://www.saucedemo.com/")

time.sleep(5)