from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

object = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=object)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.google.com/")
driver.find_element(By.NAME,"q").send_keys("selenium")
driver.find_element(By.NAME,"q").click()

driver.find_element(By.XPATH,"//h3[normalize-space()='Selenium']").click()
