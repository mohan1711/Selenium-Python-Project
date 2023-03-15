import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://demoqa.com/buttons")

dc_button = driver.find_element(By.ID,"doubleClickBtn")
act = ActionChains(driver)

act.double_click(dc_button).perform()

time.sleep(5)