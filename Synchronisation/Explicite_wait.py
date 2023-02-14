import time
from selenium.common import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
my_wait=WebDriverWait(driver,20,poll_frequency=2,ignored_exceptions=[NoSuchElementException])
#driver.implicitly_wait(10)
driver.get("https://www.google.ca")
#driver.find_element(By.XPATH,'//input[@name="q"]').send_keys("selenuim")

search_google=my_wait.until(EC.presence_of_element_located((By.NAME,'q')))

#search_google=driver.find_element(By.NAME,'q')
search_google.send_keys("selenuim")
search_google.submit()
#linkresult=driver.find_element(By.XPATH,'//h3[text()="Selenium"]')

linkresult=my_wait.until(EC.presence_of_element_located((By.XPATH,'//h3[text()="Selenium"]')))
linkresult.click()
driver.close()