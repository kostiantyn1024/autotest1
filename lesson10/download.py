import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
download_directory = os.path.join(os.getcwd(), "download")
preferences = {
    "download.default_directory": download_directory
}
chrome_options.add_experimental_option("prefs", preferences)
chrome_options.add_argument("--window-size=1920,1080")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("https://demoqa.com/upload-download")
time.sleep(3)

download_file = driver.find_element("xpath", "//a[@id='downloadButton']")
download_file.click()

time.sleep(3)