from bs4 import BeautifulSoup
import requests as rq
root = "https://subslikescript.com"
web = f'{root}/movies_letter-A'
get = rq.get(web)
content = get.text
soup = BeautifulSoup(content, 'lxml')
ul = soup.find("ul",class_= "pagination")
li = ul.find_all("li",class_="page-item")
last_page = li[-2].text 
box = soup.find('article', class_='main-article') 
links = []
for i in range(1,int(last_page)+1)[:2]: # Se toman todas las paginaciones en este caso se estan tomandos solo 2 de las 1000 paginas ya que son muchas.
    get = rq.get(f'{web}?page={i}') # Se acorta la ruta web por el enlace directo y se mencinan los numeros de paginacion
    content = get.text # Se obtiene el contenido tipo texto
    soup = BeautifulSoup(content, 'lxml')
    for link in box.find_all('a', href=True): # Conseguir todos los elementos de un elemento.
        links.append(link['href']) # Se toman los links href de las paginas para meterse a los links
    for link in links: # Se recorren los links
        try:
            print(link) # Vista de los links extraidos
            get = rq.get(f'{root}/{link}') # Se adentra a cada link extraido de las paginaciones
            content = get.text # Se saca el texto
            soup = BeautifulSoup(content, 'lxml')
            box = soup.find('article', class_='main-article') 
            h1 = box.find('h1').get_text()
            script = box.find('div',class_= 'full-script').get_text(strip=True, separator=' ')
        except:
            print("Link no funcionando")  # Se hace un Try donde se caputa los links que no esten funcionando
            print(link)
        try:
            with open(rf'Seccion_3/scripts/{str(h1)}.txt','w') as arch: # Se escriben los scripts
                arch.write(str(script))
        except UnicodeEncodeError: # Try que captura el error utf-8 de algunos elementos
            with open(rf'Seccion_3/scripts/{str(h1)}.txt','w', encoding='utf-8') as arch:
                arch.write(str(script))
        except OSError: # Error de script No funcionando para su escritura
            print("Link Not Work")