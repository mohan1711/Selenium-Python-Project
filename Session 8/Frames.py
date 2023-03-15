import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Frames.html")
time.sleep(5)

########Single frame
# driver.switch_to.frame("singleframe")
# driver.find_element(By.XPATH,"//input[@type='text']").send_keys("frames")
# time.sleep(5)

#********** Inner frame or Nested frame

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()
time.sleep(5)

outer_frame = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outer_frame)
time.sleep(5)

inner_frame = driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(inner_frame)
time.sleep(5)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Nested Frame found")
time.sleep(5)

# driver.switch_to.parent_frame()     #Used to switch to parent frame - available in selenium 4
