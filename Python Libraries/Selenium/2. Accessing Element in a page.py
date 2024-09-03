"""
To get the element from webpage , below is the priority list to look for in HTML:- 

1. ID
2. Name
3. Class       (selenium give the 1st element that it finds in a website , class is not necessarily unique)
"""

from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By  
import time  

driver = webdriver.Chrome()  
driver.get("https://www.python.org/doc/")               # Opening the specified URL in the browser

search = driver.find_element(By.ID, "id-search-field")  # Finding the search bar on the page using the element "id"
search.send_keys("pycon")                               # Typing "pycon" on the search bar
search.send_keys(Keys.RETURN)                           # Simulating pressing the Enter key using the `Keys.RETURN` constant.

time.sleep(10)  # Adding a wait time of 10 seconds

driver.quit()  # Quitting the browser and closing the webdriver instance