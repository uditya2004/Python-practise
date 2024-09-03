from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By  
import time  

driver = webdriver.Chrome()  
driver.get("https://www.python.org/doc/")               # Opening the specified URL in the browser

search = driver.find_element(By.ID, "id-search-field")  # Finding the search bar on the page using the element "id"
search.send_keys("pycon")                               # Typing "pycon" on the search bar
search.send_keys(Keys.RETURN)                           # Simulating pressing the Enter key using the `Keys.RETURN` constant.

main = driver.find_element(By.CSS_SELECTOR, ".list-recent-events.menu")

# Find all list items (li elements) inside the results list
events = main.find_elements(By.TAG_NAME, "li")

# Print the text of each event
for event in events:
    print(event.text)

time.sleep(10)  # Adding a wait time of 10 seconds

driver.quit()  # Quitting the browser and closing the webdriver instance