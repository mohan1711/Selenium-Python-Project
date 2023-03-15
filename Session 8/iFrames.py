#Task. https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html

# In the above link of 1st iframe click on org.openqa.selenium
# In the second iframe click on webdriver
# In the third iframe click on help

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
time.sleep(5)

driver.switch_to.frame("packageListFrame")
driver.find_element(By.XPATH,"//a[normalize-space()='org.openqa.selenium']").click()
driver.switch_to.default_content()
time.sleep(5)

driver.switch_to.frame("packageFrame")
driver.find_element(By.XPATH,"//span[normalize-space()='WebDriver']").click()
driver.switch_to.default_content()
time.sleep(5)

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH,"/html[1]/body[1]/header[1]/nav[1]/div[1]/div[1]/ul[1]/li[8]/a[1]").click()
driver.switch_to.default_content()
time.sleep(5)










