
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
# driver.implicitly_wait(10)

driver.get("https://www.nopcommerce.com/en")
time.sleep(5)
downloads = driver.find_element(By.XPATH,"//span[normalize-space()='Downloads']")
dwn_nopcom = driver.find_element(By.XPATH,"//span[normalize-space()='Download nopCommerce']")


# Normal way to open link in same tab
# act = ActionChains(driver)
# act.move_to_element(downloads).move_to_element(dwn_nopcom).click().perform()

# To open link download nop commerce in new tab
act = ActionChains(driver)
act.move_to_element(downloads).move_to_element(dwn_nopcom).key_down(Keys.CONTROL).click().key_up(Keys.CONTROL).perform()

time.sleep(10)