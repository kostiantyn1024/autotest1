import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://demoqa.com/dynamic-properties")

wisible_after_button = ("xpath", "//button[@id='visibleAfter']")
wait.until(EC.visibility_of_element_located(wisible_after_button)).click()

time.sleep(10)

enable_in_second = ("xpath", "//button[@id='enableAfter']")
wait.until(EC.element_to_be_clickable(enable_in_second)).click()

