import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
browser = webdriver.Chrome(service=service)

browser.get("https://elzero.org")

browser.find_element(By.ID, "search").send_keys('Front-End Developer')

browser.implicitly_wait(3)

browser.find_element(By.CSS_SELECTOR, ".search-submit").click()

browser.implicitly_wait(3)

num_of_results = browser.find_element(By.CSS_SELECTOR, ".container h2 span:first-child")

browser.implicitly_wait(3)

print(num_of_results.get_attribute('innerHTML'))

browser.quit()