import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

#JS alert
driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)

# JS Decline
driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(2)


#JS prompt
driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()

alertwindow = driver.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("Welcome")
alertwindow.accept()



