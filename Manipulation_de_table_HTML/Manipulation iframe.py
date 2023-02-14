import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.switch_to.frame('packageListFrame')
driver.find_element(By.XPATH,"//a[text()='org.openqa.selenium']").click()
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame('packageFrame')
driver.find_element(By.XPATH,"//span[text()='WebDriver']").click()
time.sleep(2)
driver.switch_to.default_content()
driver.switch_to.frame('classFrame')
driver.find_element(By.XPATH,"//a[text()='Help']").click()
time.sleep(4)
