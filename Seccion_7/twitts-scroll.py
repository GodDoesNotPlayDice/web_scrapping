from selenium import webdriver as wb
import pandas as pd
import time as t
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

path = 'C:/Users/Xikota/Downloads/chromedriver'
web = 'https://twitter.com/search?q=python&src=typed_query'
driver = wb.Chrome(path)
driver.get(web)
# t.sleep(5)
last_height = driver.execute_script("return document.body.scrollHeight")

#tweets = driver.find_elements_by_xpath('//article[@role="article"]')
data = []
tweet_ids = set()
scrolling = True
while scrolling:
    tweets = WebDriverWait(driver, 5).until(Ec.presence_of_all_elements_located((By.XPATH, '//article[@role="article"]')))
    for i in tweets[-15:]:
        a = i.find_element_by_xpath(".//span[contains(text(), '@')]").text
        b = " ".join((i.find_element_by_xpath(".//div[@data-testid='tweetText']").text).split())
        tweet_id = ''.join([a,b])
        if tweet_id not in tweet_ids:
            tweet_ids.add(tweet_id)
            data.append([a,b])
    while True:
        # Desplazar hacia la parte más baja de la pagina
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Esperar hasta que la pagina cargue
        t.sleep(2)
        # Calcular la nueva altura de desplazamiento (new_height) y compararla con la ultima altura de desplazamiento (last_height)
        new_height = driver.execute_script("return document.body.scrollHeight")
        # Si la nueva altura (new_height) es igual a la ultima altura (last_height), significa que ya no hay mas paginas entonces dejamos de hacer "scrolling"

        #if new_height == last_height:
        #    scrolling = False
        #    break
        if len(data) > 60:
            scrolling = False
            break
        else:
            last_height = new_height
            break
t.sleep(2)
driver.quit()
dataFrame = pd.DataFrame({'user': [i[0] for i in data], 'tweet': [i[1] for i in data]})
dataFrame.to_csv('Tweets-scroll.csv', index=False)
print(data)