import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()


driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

rome = driver.find_element(By.ID,"box6")
italy = driver.find_element(By.ID,"box106")
washington = driver.find_element(By.ID,"box3")
united_states = driver.find_element(By.ID,"box103")

act = ActionChains(driver)
act.drag_and_drop(rome,italy).perform()
act.drag_and_drop(washington,united_states).perform()

time.sleep(5)
