from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
chrome_driverpath = "C:\\chromedriver_win32\\chromedriver.exe"
ser = Service(chrome_driverpath)
# so screen doesn't shuts quickly
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ser)

# from datetime import datetime, timedelta
# t = datetime.now()
# min = t.strftime("%H:%M:%S").split(":")[1]
# target = int(min) + 1
# def z():
#     if min == target:
#         return True
import time
timeout = time.time() + 1
five_min = time.time() + 60*1

def z():
    if time.time() > five_min:
        # cookie_per_s = driver.find_element_by_id("cps").text
        # print(cookie_per_s)
        return False

driver.get("https://orteil.dashnet.org/cookieclicker/")
# lan = driver.find_element(By.CSS_SELECTOR,".langSelectButton title langSelect-EN")
driver.implicitly_wait(10)
driver.find_element(By.ID, "langSelect-EN").click()
# print(lan)
# lan.click()
button = driver.find_element(By.ID,"bigCookie")
while z:
    button.click()
