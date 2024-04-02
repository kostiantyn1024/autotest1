import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.freeconferencecall.com/global/pl/")

login_button = driver.find_element("xpath", "//a[@id='login-desktop']" )
login_button.click()

email_field = driver.find_element("xpath", "//input[@id='login_email']")
email_field.send_keys("dfsdf@sfdf")

print(email_field.get_attribute("maxlength"))

email_field.clear()

email_field.send_keys("sdfsdfsdf")

time.sleep(2)