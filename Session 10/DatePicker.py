import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://jqueryui.com/datepicker/")      #Also practice dummy ticket date picker

frame = driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
driver.switch_to.frame(frame)

# Method 1
# driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("03/21/2023")

# Method 2

year = "2020"
month = "November"
date = "17"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()


#Select month and year
while True:
    mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break;
    else:
        # time.sleep(1)
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()

# Select date

my_date = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody//tr//td//a")

for ele in my_date:
    if ele.text==date:
        ele.click()
        break

print(mon,' ',my_date,' ',yr,' ')

time.sleep(5)