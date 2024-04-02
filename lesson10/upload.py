import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://demoqa.com/upload-download")


upload_file = driver.find_element("xpath", "//input[@id='uploadFile']")
upload_file.send_keys(os.path.join(os.getcwd(), "download/sampleFile.jpeg"))
time.sleep(3)