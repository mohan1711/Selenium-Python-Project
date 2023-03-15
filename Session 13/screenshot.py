

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

driver.get("https://www.saucedemo.com/")
# driver.save_screenshot("C:/Users/com/PycharmProjects/Selenium_Project/Session 13/saucedemo.png")

driver.save_screenshot(os.getcwd()+"/saucedem.png")         # method 1
driver.get_screenshot_as_file(os.getcwd()+"/saucedem.png")      # method 2

driver.close()