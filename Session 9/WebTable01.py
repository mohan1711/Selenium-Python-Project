#******* Tasks

# 1. Count no of rows and columns
# 2. Read specific row and column data
# 3. Read all the row and column data
# 4. Read data based on condition - list book name whose author is mukesh



import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)

#TASK 1 Total number of rows and columns data
# rows = driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
# print('total rows ', len(rows))     #7
# time.sleep(2)
#
# columns = driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr//th")
# print('total columns ', len(columns))       #4
# time.sleep(1)

#2 TASK 2 Specific row and column data

# sp_data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[7]//td[1]").text
# print(sp_data)  #Master in JS

#3 TASK 3 Read all the data from rows and columns
# for dynamically adding value into xpath
#     1. convert varibale into string r = str(r)
#     2. keep the str in double quote = "str(r)"
#     3. add + operator before and after str(r)

# print('all the row data and column data are.................')
#
# rows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
# print('total rows ', rows)     #7
# time.sleep(2)
#
# columns = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]//th"))
# print('total columns ', columns)       #4
# time.sleep(2)
#
# for r in range(2,rows+1):
#     for c in range(1,columns+1):
#         all_data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]//td["+str(c)+"]").text
#         print(all_data,end='    ')
#     print()

#all the row data and column data are.................
# total rows  7
# total columns  4
# Learn Selenium    Amit    Selenium    300
# Learn Java    Mukesh    Java    500
# Learn JS    Animesh    Javascript    300
# Master In Selenium    Mukesh    Selenium    3000
# Master In Java    Amod    JAVA    2000
# Master In JS    Amit    Javascript    1000

# TASK 4. Read data based on condition - list book name whose author is mukesh

rows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
time.sleep(2)

for r in range(2,rows+1):
    price = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]//td[4]").text
    if price == "500":
        bookname = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]//td[1]").text
        print(bookname,"     ",price)       #Learn Java       500
    print()














