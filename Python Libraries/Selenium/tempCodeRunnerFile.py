from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

search = driver.find_element_by_id("docsearch-input")
search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(10)

driver.quit()