from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.google.com")

multi_search_txtbox = driver.find_elements(By.XPATH, "//textarea")

multi_search_txtbox[0].send_keys("IMCC")
multi_search_txtbox[0].send_keys(Keys.ENTER)   
