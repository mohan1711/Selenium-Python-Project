import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://www.opencart.com/index.php?route=account/register")
time.sleep(5)

f_name = driver.find_element(By.NAME,"firstname")
l_name = driver.find_element(By.NAME,"lastname")

f_name.send_keys("Keyboard actions")

act = ActionChains(driver)

#1 CTRL A

act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()
time.sleep(2)

#2 CTRL C

act.key_down(Keys.CONTROL)
act.send_keys("x")
act.key_up(Keys.CONTROL)
act.perform()
time.sleep(2)

# Tab

act.send_keys(Keys.TAB).perform()
time.sleep(2)

# Ctrl V

act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()

time.sleep(10)












