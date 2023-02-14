import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.ca")
#driver.find_element(By.XPATH,'//input[@name="q"]').send_keys("selenuim")
search_google=driver.find_element(By.NAME,'q')
search_google.send_keys("selenuim")
search_google.submit()
linkresult=driver.find_element(By.XPATH,'//h3[text()="Selenium"]')
linkresult.click()


#time.sleep(2)