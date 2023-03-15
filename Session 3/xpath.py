import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get('https://www.saucedemo.com/')
time.sleep(5)
#absolute xpath
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]").send_keys('standard_user')
#relative xpath
driver.find_element(By.XPATH,"//input[@id='password']").send_keys('secret_sauce')
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='login-button']").click()
time.sleep(5)

