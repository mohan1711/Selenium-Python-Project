from selenium import webdriver



def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe")
    ops = webdriver.ChromeOptions()
    ops.headless = True
    driver = webdriver.Chrome(service=serv_obj,options=ops)
    return driver

driver = headless_chrome()
driver.get("https://www.saucedemo.com/")
print(driver.title)
print(driver.current_window_handle)
print(driver.current_url)
