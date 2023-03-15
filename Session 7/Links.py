import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")

# driver.find_element(By.LINK_TEXT,"Digital downloads").click()

# driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

time.sleep(5)

links = driver.find_elements(By.TAG_NAME,'a')
for link in links:
    print(link.text)