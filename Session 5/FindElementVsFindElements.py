import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
time.sleep(5)

# find element - to find only one element
# element = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# element.send_keys('iphone 13')
# driver.find_element(By.XPATH,"//button[normalize-space()='Search']").click()
# time.sleep(5)

# find element - sending xpath of all elements but returns first element as we use find element
# element = driver.find_element(By.XPATH,"//div[@class='footer']//a") #Sitemap
# print(element.text) #Sitemap

# find elements - it is used to find multiple web elements
# To find all elements
# element = driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(len(element))
# for all_ele in element:
#     print(all_ele.text)

#  To find only one or two elements from find elements
# element = driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(element[1].text)      #Shipping & returns
# print(element[5].text)      #Contact us



