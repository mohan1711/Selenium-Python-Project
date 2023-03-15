import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
time.sleep(2)

# Type 1: Scrolling page by pixel
# driver.execute_script("window.scrollBy(0,3000)","")
# value = driver.execute_script("return window.pageYOffset;")   #to know the value of pixels
# print('the number of pixels moved ',value)
# time.sleep(10)

# Type 2: Scroll down until the element
# flag = driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# value = driver.execute_script("return window.pageYOffset;")   #to know the value of pixels
# print('the number of pixels moved ',value)      #the number of pixels moved  4866.66650390625
# time.sleep(10)

# Type 3: Scroll till the end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
# back to the starting of the page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(5)