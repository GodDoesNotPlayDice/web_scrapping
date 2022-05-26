from bs4 import BeautifulSoup
import requests as rq

web = 'https://subslikescript.com/movie/Titanic-120338'
get = rq.get(web)
content = get.text
soup = BeautifulSoup(content, 'lxml')
box = soup.find('article', class_= 'main-article')
h1 = box.find('h1').get_text()
script = box.find('div',class_='full-script').get_text(strip=True, separator=' ')
with open(f'Seccion_3/{h1}.txt','w',encoding='utf-8') as f:
    f.write(script)