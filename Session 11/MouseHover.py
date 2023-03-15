import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.jainuniversity.ac.in/")

about = driver.find_element(By.ID,"navbarDropdownMenuLink")
leadership = driver.find_element(By.XPATH,"//a[normalize-space()='Leadership']")
chancellor = driver.find_element(By.XPATH,"//a[normalize-space()='Chancellor']")

act = ActionChains(driver)

act.move_to_element(about).move_to_element(leadership).move_to_element(chancellor).click().perform()

time.sleep(5)