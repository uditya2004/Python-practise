import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from groq import Groq
import subprocess
from selenium.webdriver.edge.service import Service

# Set the API key as an environment variable
os.environ["GROQ_API_KEY"] = "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"

# Initialize Groq API client using the environment variable
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

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
    # Clean the list to remove numbers and extra spaces
    words = [word.split(".")[1].strip() if "." in word else word.strip() for word in words if word.strip()]
    return words

# Function to launch the Edge browser in debugging mode
def launch_edge_with_debugging():
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"  # Adjust if necessary
    debug_port = 9222  # A common debugging port, can be changed if needed

    # Launch Edge with remote debugging enabled
    subprocess.Popen([edge_path, f"--remote-debugging-port={debug_port}", "--user-data-dir=C:\\EdgeDebug"])

    return debug_port

# Launch Edge with debugging
debug_port = launch_edge_with_debugging()

# Wait for a few seconds to ensure Edge has launched
time.sleep(5)

# Set up the WebDriver options to attach to the debug port
options = webdriver.EdgeOptions()
options.use_chromium = True
options.add_experimental_option("debuggerAddress", f"127.0.0.1:{debug_port}")

# Initialize the WebDriver by attaching to the running Edge instance
driver = webdriver.Edge(options=options)
driver.get("https://www.bing.com")

# Generate the list of random words
random_words = generate_random_words_list()

# Loop to search each word one at a time, starting from the 2nd element
for word in random_words[1:]:  # Skip the first element
    # Step 2: Perform the search with just the random word
    search_bar = driver.find_element("name", "q")
    search_bar.clear()  # Clear the previous search term
    search_bar.send_keys(word)
    
    # Step 3: Wait for 2 seconds before hitting search
    time.sleep(2)
    
    # Hit search
    search_bar.send_keys(Keys.RETURN)
    
    # Step 4: Wait for 7 seconds before moving to the next word
    time.sleep(5)

# Close the browser after the loop is done
driver.quit()
