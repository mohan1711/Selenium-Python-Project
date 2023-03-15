
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://ps.uci.edu/~franklin/doc/file_upload.html")
time.sleep(5)

driver.find_element(By.XPATH,"//input[@name='userfile']").send_keys("C:/Users/com/Videos/Mohan_Babu_Resume.pdf")

time.sleep(10)
