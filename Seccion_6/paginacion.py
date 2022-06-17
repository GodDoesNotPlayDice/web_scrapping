from selenium import webdriver as wb
from selenium.webdriver.chrome.options import Options #Handlesss
import pandas as pd
import time as t
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = Options() #Handless
options.headless = False # Handless
# options.add_argument('window-size=1920x1080') # Para el handless
web = "https://www.audible.com/search"
path = 'C:/Users/Xikota/Downloads/chromedriver'
driver = wb.Chrome(path, options=options)
driver.get(web)
driver.maximize_window() # Utilizando otro
# Paginacion
paginacion = driver.find_element_by_xpath('//ul[contains(@class, "pagingElements")]')
pages = paginacion.find_elements_by_tag_name('li')
last_page = int(pages[-2].text)
# next_page = driver.find_element_by_xpath('//span[contains(@class, "nextButton")]')
books = []
current_page = 1

while current_page <= last_page:
    t.sleep(2) # Espera implicita
    cont = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "adbl-impression-container"))) # Espera explicita
    #cont = driver.find_element_by_class_name('adbl-impression-container ')
    stock = WebDriverWait(cont, 3).until(EC.presence_of_all_elements_located((By.XPATH, "./li")))
    #tock = cont.find_elements_by_xpath('./li')
    for i in stock:
        a = i.find_element_by_xpath('.//h3[contains(@class, "bc-heading")]').text
        b = i.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text
        c = i.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text
        books.append([a,b,c])
    current_page+=1
    try:
        next_page = driver.find_element_by_xpath('.//span[contains(@class , "nextButton")]')
        next_page.click()
    except:
        pass

# for i in stock: Single
#     a =i.find_element_by_xpath('.//h3[contains(@class, "bc-heading")]').text
#     b = i.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text
#     c = i.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text
#     books.append([a,b,c])
driver.quit()
df = pd.DataFrame({'title':[i[0] for i in books], 'Author': [i[1] for i in books], 'Duracion': [i[2] for i in books]})
df.to_csv('Seccion_6/books.csv', index=False)






