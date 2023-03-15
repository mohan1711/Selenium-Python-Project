import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://www.opencart.com/index.php?route=account/register")

drop_country_select = driver.find_element(By.ID,'input-country')

drop_country = Select(drop_country_select)

# These are the built in functions - 3 types
# drop_country.select_by_visible_text("India")
# drop_country.select_by_value('99')
# drop_country.select_by_index(99)
# time.sleep(5)

# Select drop down element India without using built method

alloptions = drop_country.options
print("The total number options are",len(alloptions))

time.sleep(5)

for choice in alloptions:
    if choice.text == "India":
        choice.click()
        break

time.sleep(5)