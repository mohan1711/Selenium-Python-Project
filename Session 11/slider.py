import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
time.sleep(2)



min_slider = driver.find_element(By.XPATH,"//span[1]")
max_slider = driver.find_element(By.XPATH,"//span[2]")

print("location of min and max slider before moving",min_slider.location,' ',max_slider.location)
#output - location of min and max slider before moving {'x': 59, 'y': 250}   {'x': 510, 'y': 250}

act = ActionChains(driver)

act.drag_and_drop_by_offset(min_slider,120,0).perform()
act.drag_and_drop_by_offset(max_slider,-50,0).perform()

print("location of min and max slider after moving",min_slider.location,' ',max_slider.location)
#output -   location of min and max slider after moving {'x': 181, 'y': 250}   {'x': 460, 'y': 250}

time.sleep(5)