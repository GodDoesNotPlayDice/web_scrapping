from selenium import webdriver as wb
import time as t
import twitts as tw
web = 'https://twitter.com/'
path = 'C:/Users/Xikota/Downloads/chromedriver'
driver = wb.Chrome(path)
driver.get(web)
driver.maximize_window()
login = driver.find_element_by_xpath("//a[@href='/login']")
t.sleep(2)
login.click()
t.sleep(5)
input_ = driver.find_element_by_xpath("//input[@autocomplete='username']")
input_.send_keys("EMAIL")
nextPage = driver.find_elements_by_xpath("//div[@role='button']")
t.sleep(2)
nextPage[2].click()
t.sleep(5)
input_ = driver.find_element_by_tag_name('input')
input_.send_keys('NAME') # Este paso es en caso de que twitter encuentre cosas inusuales
nextPage = driver.find_elements_by_xpath("//div[@role='button']")
t.sleep(2)
nextPage[1].click()
t.sleep(5)
input_ = driver.find_element_by_xpath("//input[@name='password']")
nextPage = driver.find_elements_by_xpath("//div[@role='button']")
t.sleep(2)
input_.send_keys('PASSWORD')
t.sleep(2)
nextPage[2].click()