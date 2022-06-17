from selenium import webdriver
import pandas as pd
import time as t
# El primer website tiene 5 paginas, mientras que el segundo tiene 60. Para obtener resultados más rápidos, testea el codigo con el primer website
web = "https://www.audible.com/search"
# web = "https://www.audible.com/search"
path = 'C:/Users/Xikota/Downloads/chromedriver'
driver = webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()
# Paginacion 1
pagination = driver.find_element_by_xpath('//ul[contains(@class, "pagingElements")]')  # localizando la barra de paginacion
pages = pagination.find_elements_by_tag_name('li')   # localizando cada pagina mostrada en la barra de paginacion
last_page = int(pages[-2].text)  # obtener la ultima pagina usando index de numeros negativos (index negativo empieza donde termina la lista)
books = []
# Paginacion 2
current_page = 1   # esta es la pagina actual (current_page) donde el bot empieza a hacer web scraping
# El "bucle while" va a trabajar hasta que el bot llegue a la ultima pagina del website, luego el bucle se cortara
while current_page <= last_page:
    t.sleep(2)  # dejar que la pagina cargue correctamente
    container = driver.find_element_by_class_name('adbl-impression-container ')
    products = container.find_elements_by_xpath('./li')
    for product in products:
        a = product.find_element_by_xpath('.//h3[contains(@class, "bc-heading")]').text
        b = product.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text
        c = product.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text
        books.append([a,b,c])
    current_page+= 1  # incrementar la pagina_actual (current_page) en 1, luego de que la data es extraida
    # Localizar el boton siguiente_pagina (next_page) y hacer click en el boton. Si el elemento no esta en la pagina, pasar a la siguiente iteracion
    try:
        next_page = driver.find_element_by_xpath('.//span[contains(@class , "nextButton")]')
        next_page.click()
    except:
        pass
driver.quit()
df = pd.DataFrame({'title':[i[0] for i in books], 'Author': [i[1] for i in books], 'Duracion': [i[2] for i in books]})
df.to_csv('Seccion_6/books.csv', index=False)
