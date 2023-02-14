import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
list_link=driver.find_elements(By.TAG_NAME,"a")
compteur=0
for ele in list_link:
    URL=ele.get_attribute("href")
    try:
        response=requests.head(URL)
    except:
        None
    if response.status_code>=400:
        print(URL," est un lien brise")
        compteur=compteur+1
    else:
        print(URL, " est un lien valide")

print("le nombre de liens brise =",compteur)


driver.close()