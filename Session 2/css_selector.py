import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)

driver.get('https://www.facebook.com/')
driver.maximize_window()
time.sleep(5)

#tag and id #Syntax: tagname#valueofid (or) #valueofid

#method 1
driver.find_element(By.CSS_SELECTOR, 'input#email').send_keys('abcde123')
#method 2
driver.find_element(By.CSS_SELECTOR, '#email').send_keys('abcde123')

#tag and class #Syntax: tagname.valueofCLass (or) .valueofClass

#method 1
driver.find_element(By.CSS_SELECTOR, 'input.inputtext').send_keys('abcde123')
#method 2
driver.find_element(By.CSS_SELECTOR, '.inputtext').send_keys('abcde123')

#tag and attribute #Syntax tagname[attribute=value]

#method 1
driver.find_element(By.CSS_SELECTOR, 'input[data-testid=royal_email]').send_keys('abcde123')
#method 2
driver.find_element(By.CSS_SELECTOR, '[data-testid=royal_email]').send_keys('abcde123')

#tag , class and attribute #Syntax tagname.valueofClass[attribute=value]

driver.find_element(By.CSS_SELECTOR, 'input.inputtext[data-testid=royal_pass]').send_keys('abcde123')
