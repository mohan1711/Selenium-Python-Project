import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from Session14 import XLUtils
from selenium.webdriver.support.select import Select

serv_obj = Service("C:/Users/com/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")

file = "C:/Users/com/Downloads/caldata.xlsx"

rows = XLUtils.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
    pric = XLUtils.readData(file,"Sheet1",r,1)
    rateofinterest = XLUtils.readData(file, "Sheet1", r, 2)
    per1 = XLUtils.readData(file, "Sheet1", r, 3)
    per2 = XLUtils.readData(file, "Sheet1", r, 4)
    fre = XLUtils.readData(file,"Sheet1",r,5)
    exp_mvalue = XLUtils.readData(file, "Sheet1", r, 6)

    driver.find_element(By.NAME,"principal").send_keys(pric)
    driver.find_element(By.NAME,"interest").send_keys(rateofinterest)
    driver.find_element(By.NAME,"tenure").send_keys(per1)

    period_drop=Select(driver.find_element(By.NAME,"tenurePeriod"))
    period_drop.select_by_visible_text(per2)

    freq = Select(driver.find_element(By.NAME,"frequency"))
    freq.select_by_visible_text(fre)

    driver.find_element(By.XPATH,"//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']").click()

    act_value = driver.find_element(By.XPATH,"//span[@id='resp_matval']//strong").text

    if float(exp_mvalue)==float(act_value):
        print('test passed')
        XLUtils.writeData(file,"Sheet1",r,8,"passed")
        XLUtils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print('test failed')
        XLUtils.writeData(file, "Sheet1", r, 8, "failed")
        XLUtils.fillGreenColor(file, "Sheet1", r, 8)
    driver.find_element(By.XPATH,"//img[@class='PL5']").click()
    time.sleep(5)





