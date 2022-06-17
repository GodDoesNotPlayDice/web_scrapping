from selenium import webdriver as wb
from selenium.webdriver.support.ui import Select
import pandas as pd
path = "C:/Users/Xikota/Downloads/chromedriver"
web = f'https://www.adamchoi.co.uk/overs/detailed'
driver = wb.Chrome(path)
driver.get(web)
button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
button.click()
dropdown = Select(driver.find_element_by_id('country'))
dropdown.select_by_visible_text('Spain')
matches = [i.text for i in driver.find_elements_by_tag_name('tr')]
driver.quit()
df = pd.DataFrame({'Matches':matches})
print(df)
df.to_csv('Matches.csv', index=False) 