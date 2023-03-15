import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("http://www.deadlinkcity.com/")

alllinks = driver.find_elements(By.TAG_NAME,'a')
count = 0

for links in alllinks:
    url = links.get_attribute('href')
    try:
        result = requests.head(url)
    except:
        None
    if result.status_code>=400:
        print(url,"is broken link")
        count+=1
    else:
        print(url,"is valid link")

print("Total number of broken links is ", count)

#### output
# C:\Users\com\PycharmProjects\Selenium_Project\venv\Scripts\python.exe "C:\Users\com\PycharmProjects\Selenium_Project\Session 7\BrokenLinks.py"
# http://www.deadlinkcity.com/comparison.asp is valid link
# http://www.deadlinkcity.com/errorlist.asp is valid link
# http://www.deadlinkcity.com/error-page.asp?e=400 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=401 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=402 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=403 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=404 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=405 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=406 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=407 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=408 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=409 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=410 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=411 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=412 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=413 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=414 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=415 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=416 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=417 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=420 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=422 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=423 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=424 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=429 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=431 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=450 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=500 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=501 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=502 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=503 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=504 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=505 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=506 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=507 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=509 is broken link
# http://www.deadlinkcity.com/error-page.asp?e=510 is broken link
# http://www.deadlinkcity.com/page-not-found.asp is broken link
# http://www.domaindoesnot.exist/ is broken link
# http://www.deadlinkcity.com/default.asp?r=1 is valid link
# http://www.deadlinkcity.com/default.asp?r=2 is valid link
# http://www.deadlinkcity.com/default.asp?r=4 is valid link
# http://www.deadlinkcity.com/default.asp?r=5 is valid link
# http://www.deadlinkcity.com/default.asp?r=6 is valid link
# http://www.deadlinkcity.com/default.asp?r=7 is valid link
# http://www.deadlinkcity.com/disallowed/disallowed.html is broken link
# http://www.deadlinkcity.com/disallowed/nonexistent.html is broken link
# mailto:info@deadlinkchecker.com?subject=DeadLinkCity.com%20-%20feedback is broken link
# Total number of broken links is  40
#
# Process finished with exit code 0
