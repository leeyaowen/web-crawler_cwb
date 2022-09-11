from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# 單一測站年月迴圈
def onestationyearloop(url, year1, year2, dpath):
    stationoptions = webdriver.ChromeOptions()
    prefs = {'download.default_directory': dpath}
    stationoptions.add_experimental_option('prefs', prefs)
    browser = webdriver.Chrome('chromedriver.exe', options=stationoptions)
    browser.maximize_window()
    year = list(range(year1, year2 + 1))
    month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    url = url.split('&altitude')
    for i in range(0, len(year)):
        for j in range(0, len(month)):
            browser.get(f'{url[0][:-7]}{str(year[i])}-{month[j]}&altitude{url[1]}')
            time.sleep(2)
            downloadbtn = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="downloadCSV"]')))
            downloadbtn.click()
            print(str(year[i]) + month[j])
            time.sleep(5)


# 單一縣市迴圈
def onecityloop(url, year1, year2, dpath):
    stationoptions = webdriver.ChromeOptions()
    prefs = {'download.default_directory': dpath}
    stationoptions.add_experimental_option('prefs', prefs)
    browser = webdriver.Chrome('chromedriver.exe', options=stationoptions)
    browser.maximize_window()
    year = list(range(year1, year2 + 1))
    month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    browser.get(url)
    selectbox = Select(browser.find_element_by_xpath('//*[@id="selectStno"]'))
    for i in range(0, len(selectbox.options)):
        selectbox = Select(browser.find_element_by_xpath('//*[@id="selectStno"]'))
        selectbox.select_by_index(i)
        cwburl = browser.current_url
        url = cwburl.split('&altitude')
        for j in range(0, len(year)):
            for k in range(0, len(month)):
                browser.get(f'{url[0][:-7]}{str(year[j])}-{month[k]}&altitude{url[1]}')
                time.sleep(2)
                downloadbtn = WebDriverWait(browser, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="downloadCSV"]')))
                downloadbtn.click()
                print(str(year[j]) + month[k])
                time.sleep(5)


while True:
    st_or_city = input('Select one station or one city? \n1. station\n2. city\n')
    download_path = input('Download path=?\n')
    startyear = input('start year=?\n')
    endyear = input('End year=?\n')
    sturl = input('URL=?\n')

    # noinspection PyBroadException
    try:
        if st_or_city == str(1):
            onestationyearloop(str(sturl).strip(), int(startyear), int(endyear), download_path)
        elif st_or_city == str(2):
            onecityloop(str(sturl).strip(), int(startyear), int(endyear), download_path)
        else:
            pass
    except Exception as e:
        print(e)
        continue