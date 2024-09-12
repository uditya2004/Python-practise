from appium import webdriver
from appium.options.common import AppiumOptions
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from groq import Groq
import os

# Set the API key as an environment variable
os.environ["GROQ_API_KEY"] = "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"

# Initialize Groq API client using the environment variable
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Function to generate a list of 50 unique random words using Groq's Llama 3.1 model
def generate_random_words_list():
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "List 50 different words from a dictionary, no two words should be the same.",
            }
        ],
        model="llama3-70b-8192",
    )
    words = chat_completion.choices[0].message.content.strip().split("\n")
    words = [word.split(".")[1].strip() if "." in word else word.strip() for word in words if word.strip()]
    return words

# Set up Appium options
appium_options = AppiumOptions()
appium_options.platform_name = 'Android'
appium_options.device_name = 'Realme_Narzo_60_Pro'
appium_options.app_package = 'com.microsoft.bing'
appium_options.app_activity = 'com.microsoft.sapphire.app.main.SapphireMainActivity'
appium_options.automation_name = 'UiAutomator2'
appium_options.no_reset = False
appium_options.full_reset = True
appium_options.auto_grant_permissions = True
appium_options.ignore_hidden_api_policy_error = True
appium_options.set_capability("disableSuppressAccessibilityService", True)
appium_options.set_capability("dontStopAppOnReset", True)
appium_options.set_capability("autoGrantPermissions", True)


# Initialize the WebDriver with the Appium options
driver = webdriver.Remote(
    command_executor="http://localhost:4723",
    options=appium_options
)

# Wait for Bing to launch
time.sleep(5)

# Use explicit wait to locate the search bar by resource-id
search_bar = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((AppiumBy.XPATH, "//*[@resource-id='com.microsoft.bing:id/search_bar']"))
)

# Generate the list of random words
random_words = generate_random_words_list()

# Start searching for each word using the Bing search bar
for word in random_words:
    search_bar.clear()
    search_bar.send_keys(word)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(5)  # Adjust the wait time as needed

# Close the session
driver.quit()
