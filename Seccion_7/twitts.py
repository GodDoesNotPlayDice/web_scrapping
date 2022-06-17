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
tweets = WebDriverWait(driver, 5).until(Ec.presence_of_all_elements_located((By.XPATH, '//article[@role="article"]')))
#tweets = driver.find_elements_by_xpath('//article[@role="article"]')
data = []
for i in tweets:
    a = i.find_element_by_xpath(".//span[contains(text(), '@')]").text
    b = " ".join((i.find_element_by_xpath(".//div[@data-testid='tweetText']").text).split())
    data.append([a,b])
driver.quit()
dataFrame = pd.DataFrame({'user': [i[0] for i in data], 'tweet': [i[1] for i in data]})
dataFrame.to_csv('Tweets.csv', index=False)
print(data)