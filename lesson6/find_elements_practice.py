import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

print(driver.find_element("class name","wikipedia-icon "))
print(driver.find_element("id","Wikipedia1_wikipedia-search-input"))
print(driver.find_element("class name","wikipedia-search-button"))
print(driver.find_elements("tag name", "button")[4])

driver.find_elements()