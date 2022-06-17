from selenium import webdriver
from time import sleep as s 
web = 'https://www.picuki.com/profile/belle.delphine'
path = 'C:/Users/Xikota/Downloads/chromedriver'
driver = webdriver.Chrome(path)
driver.get(web)
driver.maximize_window()
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Desplazar hacia la parte más baja de la pagina
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Esperar hasta que la pagina cargue
    s(5)
    # Calcular la nueva altura de desplazamiento (new_height) y compararla con la ultima altura de desplazamiento (last_height)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:  # Si la nueva altura (new_height) es igual a la ultima altura (last_height), significa que ya no hay mas paginas entonces dejamos de hacer "scrolling"
        break
    else:
        last_height = new_height
s(5)
driver.quit()