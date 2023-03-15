import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(5)

