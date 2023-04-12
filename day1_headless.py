# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 03:00:19 2023

@author: hp
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
#import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#imports for headless
from webdriver_manager.chrome import ChromeDriverManager


opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

#Specify the browser to use
driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)

#Enter url of website for scraping
driver.get("https://python.org")
#Enter url of website for scraping
driver.get("https://python.org")

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

socialize_btn = driver.find_element(By.CLASS_NAME, "action-trigger")

driver.find_element(By.ID, "news").click()

top_blog = driver.find_element(By.CLASS_NAME, "event-title").text

print("value of top blog is : " +str(top_blog))
