import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe/")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.get("https://www.selenium.dev/documentation/webdriver/interactions/windows/")
driver.implicitly_wait(5)
# windowID = driver.current_window_handle
# print(windowID) #241EA8E996E5F8AC00F5502A600495BE - it is dynamic and randomly generated

# Handling mutliple windows
driver.find_element(By.XPATH,"//a[normalize-space()='new window']").click()

WindowIDS = driver.window_handles

#Approach 1:
# parent_win = WindowIDS[0]
# child_win = WindowIDS[1]
#
# print(parent_win, child_win)    #CDwindow-A73DFE9DD8860BA029B54EE04E429D1E CDwindow-6376D8491D611EA94423B9C77178EA2F
#
# driver.switch_to.window(child_win)
# print('The child window is ',driver.title)      #The child window is  Selenium
#
# driver.switch_to.window(parent_win)
# print('The parent window is ',driver.title)     #The parent window is  Working with windows and tabs | Selenium

#Approach 2:

# for winID in WindowIDS:
#     driver.switch_to.window(winID)
#     print(driver.title)
#     print(driver.window_handles)
#
# time.sleep(5)

### Output
# Working with windows and tabs | Selenium
# ['CDwindow-E7D6F41D6510B3DA9FBADA1DFB543558', 'CDwindow-8DF4AE583BF7E5D438C8FB7C9322CE0C']
# Selenium
# ['CDwindow-E7D6F41D6510B3DA9FBADA1DFB543558', 'CDwindow-8DF4AE583BF7E5D438C8FB7C9322CE0C']


# Approach 3: close one particular window
for winID in WindowIDS:
    driver.switch_to.window(winID)
    if driver.title=="Selenium":
        driver.close()

time.sleep(5)