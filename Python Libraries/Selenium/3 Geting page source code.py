from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By  
import time  

driver = webdriver.Chrome()  

driver.get("https://www.python.org/doc/")               

print(driver.page_source)         #Printing the entire page source code

time.sleep(10)  # Adding a wait time of 10 seconds

driver.quit()  # Quitting the browser and closing the webdriver instance