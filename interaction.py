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


WIKI = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(WIKI)
no = driver.find_elements(By.CSS_SELECTOR,"#articlecount a")
for a in no:
    count = a.text[0]
    # print(count)
    # a.click()
search = driver.find_element(By.NAME,"search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

LOGIN = "https://web.archive.org/web/20220120120408/http://secure-retreat-92358.herokuapp.com/"
driver.get("https://web.archive.org/web/20220120120408/http://secure-retreat-92358.herokuapp.com/")
firstn = driver.find_element(By.NAME,"fName")
# firstn.send_keys("AVIII")
# lastn = driver.find_element(By.NAME,"lName")
# lastn.send_keys("GOMEZ")
# email = driver.find_element(By.NAME,"email")
# email.send_keys("aviiigomez@gmail.com")
# email.send_keys(Keys.TAB)
# email.send_keys(Keys.ENTER)

firstn.send_keys('TestFirstName', Keys.TAB, 'TestLastName', Keys.TAB, 'TestEmail@gmail.com', Keys.TAB, Keys.ENTER)



# driver.quit()