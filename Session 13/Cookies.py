import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")

cookies = driver.get_cookies()
print("Size of cookies", len(cookies))      #Size of cookies 5

# To get all cookies
# for c in cookies:
#     # print(c)
#     print(c.get('domain'),":",c.get('httpOnly'))

# To add cookies
driver.add_cookie({'name':'mycookie','value':'123456'})
cookies = driver.get_cookies()
print("Size of cookies after adding", len(cookies))     #Size of cookies after adding 6

# To delete particular cookie
driver.delete_cookie('mycookie')
cookies = driver.get_cookies()
print("Size of cookies after deleting", len(cookies))       #Size of cookies after deleting 5


# To delete all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("Size of cookies after delete all cookies", len(cookies))     #Size of cookies after delete all cookies 0

driver.quit()
