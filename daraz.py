from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

driver = webdriver.Chrome()
# driver = webdriver.Firefox()

driver.get('https://www.daraz.com.bd/routers/?page=1')
# driver.get('https://www.daraz.com.bd/routers/?page=1')

driver.maximize_window()

time.sleep(3)

title = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a').text

link = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a').get_attribute('href')

price = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/span').text

# sold = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[5]/span[1]/span[1]').text
# rating = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[5]/div')
# image = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/a/div/img').get_attribute('src')

image = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/a/div/img').get_attribute('src')

print(title, link, price, image)

img = requests.get(image).content
filename = title[:50].replace(" ", "_").replace("/", "_") + '.jpg' 
with open(filename, 'wb') as handler:
    handler.write(img)

print(f"Image saved as {filename}")

time.sleep(20)