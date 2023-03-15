import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj,options=ops)

driver.maximize_window()
driver.get("https://www.whatmylocation.com/")
time.sleep(5)