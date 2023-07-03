from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
chrome_driverpath = "C:\\chromedriver_win32\\chromedriver.exe"

ser = Service(chrome_driverpath)
# driver = webdriver.Chrome(service=ser)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ser)
# driver.maximize_window()

# driver.get method opens up the url automatically in your specified browser.
driver.get(url="https://www.python.org")
# driver.find_elements(class_="search-field")
# av = driver.find_elements(By.CSS_SELECTOR,".medium-widget.event-widget.last > div > ul > li > time")

# driver.quit() #shuts the entire browser
# driver.close()  #shuts the particular tab
events = {}

upcoming_events_date = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last > div > ul > li > time")
upcoming_events_name = driver.find_elements(By.CSS_SELECTOR, ".medium-widget.event-widget.last > div > ul > li > a")
for n in range(len(upcoming_events_date)):
    events[n] = {
        "time": upcoming_events_date[n].get_attribute("datetime").split("T")[0],
         "name": upcoming_events_name[n].text,
}
print(events)
driver.quit()