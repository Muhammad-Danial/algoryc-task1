# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
#import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

#imports for headless
from webdriver_manager.chrome import ChromeDriverManager

opt = webdriver.ChromeOptions()

service = Service(ChromeDriverManager().install())
#Specify the browser to use
driver = webdriver.Chrome(service=service, options=opt)

driver.maximize_window()

#Enter url of website for scraping
driver.get("https://www.albertsons.com/shop/aisles/dairy-eggs-cheese.177.html")

#whats the name r title of the page
print(driver.title)

#get a html element by its specific named defined for it by inspecting
search_bar = driver.find_element("name", "q")

#searching on the search_bar by clearing and quering it
#search_bar.clear()
#search_bar.send_keys("getting started with python")
#search_bar.send_keys(Keys.RETURN)

#current url after quering the serach bar
print(driver.current_url)

#accepting all cookies by clicking the button
driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

#closing the pop up
driver.find_element(By.ID, "onboardingCloseButton").click()

products = driver.find_elements(By.XPATH, '//*[@id="lazy-wrapper_1"]/div/product-carousel/div/div/div/div[1]')

'''for product in products:
    title = product.find_element(By.XPATH, '//*[@id="lazy-wrapper_1"]/div/product-carousel/div/div/div/div[1]')
    print(str(title))
print(product)'''
