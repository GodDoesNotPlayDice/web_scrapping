from selenium import webdriver as wb
path = "C:/Users/Usuario/Downloads/chromedriver"
web = f'https://es.investing.com/crypto/'
driver = wb.Chrome(path)
driver.get(web)
element = driver.find_elements_by_class_name("odd")
with open("content.txt","+a") as f:
    for i in element:
        f.write(str(i))
    f.close()
driver.close()
 