import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://itera-qa.azurewebsites.net/home/automation")
time.sleep(5)

#Selecting only one checkbox
# driver.find_element(By.ID,'monday').click()
# time.sleep(5)

#Selecting multiple checkboxes and unselecting them
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")

# for selecting
for checkall in checkboxes:
    time.sleep(2)
    checkall.click()
time.sleep(5)

# for un selecting
for checkall in checkboxes:
    if checkall.is_selected():
        time.sleep(2)
        checkall.click()
time.sleep(5)


# Select only monday and sunday
# checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
#
# for checkall in checkboxes:
#     weekname = checkall.get_attribute('id')
#     if weekname=='monday' or weekname=='sunday':
#         time.sleep(2)
#         checkall.click()
# time.sleep(5)

# Select only last three checboxes
# checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
#
# for i in range(len(checkboxes)-3,len(checkboxes)):
#     time.sleep(2)
#     checkboxes[i].click()

# Select only first three checboxes
# checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
#
# for i in range(len(checkboxes)):
#     if i<2:
#         time.sleep(2)
#         checkboxes[i].click()




