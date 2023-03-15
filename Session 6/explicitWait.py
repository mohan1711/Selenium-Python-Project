######## If the element is present

# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# object = Service("C:/Users/com/Downloads/chromedriver.exe/")
# driver = webdriver.Chrome(service=object)
# driver.maximize_window()
#
# mywait = WebDriverWait(driver,10)
#
# driver.get("https://www.google.com/")
# driver.find_element(By.NAME,"q").send_keys("selenium")
# driver.find_element(By.NAME,"q").submit()
#
# search = mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
#
# search.click()
#
# time.sleep(5)
#
# driver.quit()


###### if the element is not present we need to handle exception using explicit wait

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

object = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=object)
driver.maximize_window()

mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[Exception])
# poll_frequency is something which will try to poll to find the element every two seconds
# poll_frequency should be less than wait time. ex 2<10.
driver.get("https://www.google.com/")
driver.find_element(By.NAME,"q").send_keys("selenium")
driver.find_element(By.NAME,"q").submit()

search = mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
search.click()
print('exception handled')
time.sleep(5)

driver.quit()
