import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://omayo.blogspot.com/")
check1=driver.find_element(By.ID,'checkbox1').is_selected()
print(check1)
time.sleep(2)
check2=driver.find_element(By.ID,'checkbox2').is_selected()
print(check2)
time.sleep(2)
check3_enabled=driver.find_element(By.ID,'but1').is_enabled()
print(check3_enabled)
time.sleep(2)
check4_displayed=driver.find_element(By.ID,'hbutton').is_displayed()
print(check4_displayed)
time.sleep(2)
driver.close()