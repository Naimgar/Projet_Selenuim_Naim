#Pratique find element---s
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.google.ca")
time.sleep(2)
driver.find_element(By.NAME,"q").send_keys("selenium")
time.sleep(2)
list_link=driver.find_elements(By.XPATH,"//ul[@role='listbox']//li/descendant::div[@role='option']/div/span")
print(len(list_link))
time.sleep(2)
for ele in list_link:
    if ele.text == "selenium webdriver":
        ele.click()

time.sleep(3)