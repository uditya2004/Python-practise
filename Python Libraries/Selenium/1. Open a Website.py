from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://selenium.dev")

print(driver.title)

#Selenium automatically closes the browser instance when it reaches the end of the code
input('Press Enter to close the browser...')        #To prevent the chrome to get closed automatically