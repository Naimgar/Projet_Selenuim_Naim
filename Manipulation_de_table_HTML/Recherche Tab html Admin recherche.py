import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(2)
driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(2)
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//span[text()="Admin"]').click()
time.sleep(3)
nb_lignes=driver.find_elements(By.XPATH,"//div[@class='oxd-table-row oxd-table-row--with-border'][@role='row']")
print(len(nb_lignes))
#nb_colonnes=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
#print(len(nb_colonnes))
#recuperer la valeur d'une cellule de la table

#valeur_cellule=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[3]/td[1]")
#print(valeur_cellule.text)
#afficher les donnees de la table
#nb_ligne=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
#nb_colonne=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//th"))
#for ele1 in range(1,nb_ligne+1):
   # for ele2 in range(1,nb_colonne+1):
       # data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(ele1)+"]/td["+str(ele2)+"]").text
       # print(data)
#nb_ligne=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
#nb_colonne=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//th"))
#for r in range(2,nb_ligne+1):
 #   for c in range(1,nb_colonne+1):
 #       data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
 #       if(data=="Amit"):
          #print(data)
 #         data2 = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[" + str(c-1) + "]").text
          #print(data2)
   #       data3 = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[" + str(c + 2) + "]").text
   #       print(data+" *** "+data2+" *** "+data3)
#time.sleep(4)