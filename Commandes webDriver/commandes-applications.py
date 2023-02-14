#Commandes liés a l'application sous test
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
page_title = driver.title
print(page_title)
url_page = driver.current_url
print(url_page)
code_page = driver.page_source
print(code_page)
time.sleep(2)
driver.close