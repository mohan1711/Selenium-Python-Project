# Open web browser
# go to page https://opensource-demo.orangehrmlive.com/
# enter user name admin
# enter password admin123
# click on login
# capture the title of the home page
# verify the title - actual and expected
# close browser


#Selenium 4 code
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)

# If we dont want to specify path like above two lines, then save the drivers in
# C:\Users\com\AppData\Local\Programs\Python\Python310\Scripts and code the below line
# driver = webdriver.Firefox()

driver.get('https://opensource-demo.orangehrmlive.com/')
time.sleep(10)
driver.find_element(By.NAME,'username').send_keys('Admin')  #Identify element
driver.find_element(By.NAME,'password').send_keys('admin123')   #Identify element
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click() #Action
time.sleep(10)
act_title = driver.title
exp_title = 'OrangeHRM'

if act_title==exp_title:
    print('login test passed')
else:
    print('login test failed')

# driver.close()