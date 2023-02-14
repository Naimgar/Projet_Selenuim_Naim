import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
#Afficher tous les liens situé sur la page web sur une liste list_link
placeholder_text=(driver.find_element(By.XPATH,"//input[@placeholder='Username']")).get_attribute("placeholder")
print(placeholder_text)
time.sleep(2)
list_link=driver.find_elements(By.TAG_NAME,'a')
print(len(list_link))
for link in list_link:
    print(link.get_attribute("href"))
driver.close()