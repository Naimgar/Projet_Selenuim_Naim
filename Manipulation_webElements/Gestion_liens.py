import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
list_link=driver.find_elements(By.TAG_NAME,"a")
print("le nombre des elements=",len(list_link))
#commence par 0 index
#print("le texte du 4 eme lien est :",list_link[3].text)

for ele in list_link:
    print(ele.text)
    print(ele.get_attribute("href"))


driver.close()