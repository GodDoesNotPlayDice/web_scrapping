from bs4 import BeautifulSoup # Importamos bs4
import requests as rq # Importamos Rquest

website = "https://subslikescript.com/movie/Titanic-120338" # Asiganmos el sitio web que queremos extrer
result = rq.get(website) # Hacemos un get del sitio web
content = result.text # Extraemos la web en texto
soup = BeautifulSoup(content, "lxml") # Soup nos permite localizar el codigo html o elementos html de la pagina, y ademas parsearla con lxml (import lxml)
# soup.prettify() # Ver el codigo html de mejor manera 

box = soup.find("article",class_ = "main-article") # Traer el titulo de la pelicula (ejemplo) / traemos todo un article
h1 = box.find('h1').get_text() # Traemos un elemento hijo dentro de el elemento padre
script = box.find('div',class_= 'full-script').get_text(strip= True, separator= ' ') # esto hara con strip() borrar espacios en blanco y con separator borrar los saltos de linea y remplazarlos por un espacio en blanco en este caso.


### https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters ###
with open(f'Seccion_2/{str(h1)}.txt','w', encoding='utf-8') as arch: # Transcribimos la informacion extraida a un archivo TXT (Importante pasar textos a encoding utf-8 sino tirara error UnicodeEncodeError.) 
    arch.write(str(script))



