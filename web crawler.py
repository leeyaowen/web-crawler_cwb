from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# 單一測站年月迴圈
def onestationyearloop(url, year1, year2):
    stationoptions = webdriver.ChromeOptions()
    prefs = {'download.default_directory': 'D:\下載'}
    stationoptions.add_experimental_option('prefs', prefs)
    browser = webdriver.Chrome('D:/chromedriver.exe', options=stationoptions)
    browser.maximize_window()
    year = list(range(year1, year2 + 1))
    month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    for i in range(0, len(year)):
        for j in range(0, len(month)):
            browser.get(url[:-7] + str(year[i]) + '-' + month[j])
            time.sleep(2)
            downloadbtn = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="downloadCSV"]')))
            downloadbtn.click()
            print(str(year[i]) + month[j])
            time.sleep(10)

