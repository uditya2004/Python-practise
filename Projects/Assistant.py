import speech_recognition as sr
import subprocess
import os
import time
import pyautogui
from groq import Groq
import win32com.client as win32
import keyboard
import pythoncom

# Set the environment variable directly for testing
os.environ["GROQ_API_KEY"] = "GROQ Key"

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Initialize Word Application
word_app = None

# Initialize the text-to-speech engine
pythoncom.CoInitialize()
speaker = win32.Dispatch("SAPI.SpVoice")

# Function to speak the text and return whether it was interrupted
def speak(text):
    speaker.Speak(text, 1)  # 1 means asynchronous (non-blocking)
    interrupted = False
    while speaker.Status.RunningState == 2:  # 2 means speech is in progress
        if keyboard.is_pressed('space'):
            speaker.Speak("", 3)  # 3 means purge all pending speech
            print("\nSpeech interrupted. Listening...")
            interrupted = True
            break
        time.sleep(0.1)
    return interrupted

# Function to get answer from Groq's API
def get_answer_from_groq(question):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ],
            model="llama3-70b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"Error fetching answer from Groq: {e}")
        return "I'm sorry, I couldn't fetch the answer."

# Function to launch applications
def launch_application(app_name):
    app_paths = {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "brave": r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
        "word": r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
        "code": r"C:\Users\ukudi\Documents\Udi\program\Microsoft VS Code\Code.exe"  
        # Add other applications here
    }

    try:
        if app_name in app_paths:
            subprocess.Popen(app_paths[app_name])
            return f"Launched {app_name}"
        else:
            return f"Could not find application: {app_name}"
    except FileNotFoundError:
        return f"Could not find application: {app_name}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Function to create a blank document
def create_blank_document():
    global word_app
    if word_app is None:
        word_app = win32.Dispatch('Word.Application')
        word_app.Visible = True
    doc = word_app.Documents.Add()
    return "Created a blank document."

# Function to write text to the Word document
def write_to_document(text):
    if word_app is None:
        return "Word is not open."
    doc = word_app.ActiveDocument
    selection = word_app.Selection
    selection.TypeText(text)
    return "Written to the document."

# Function to search in the browser
def search_in_browser(query):
    time.sleep(5)  # Wait for the browser to open
    pyautogui.write(query)
    pyautogui.press('enter')

# Main function to run the assistant
def voice_assistant():
    browser_opened = None
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            print("Recognizing...")
            query = recognizer.recognize_google(audio).lower()

            if "stop" in query:
                speak("Goodbye!")
                break

            if "open" in query or "launch" in query:
                app_name = query.replace("open", "").replace("launch", "").strip()
                response = launch_application(app_name)
                if app_name in ["brave", "chrome"]:
                    browser_opened = app_name
            elif "create blank document" in query or "blank document" in query:
                response = create_blank_document()
            elif "write" in query:
                topic = query.replace("write", "").strip()
                answer = get_answer_from_groq(topic)
                response = write_to_document(answer)
            elif "search" in query and browser_opened:
                search_query = query.replace("search", "").strip()
                search_in_browser(search_query)
                response = f"Searching for {search_query}"
            elif browser_opened:
                search_in_browser(query)
                response = f"Searching for {query}"
            else:
                response = get_answer_from_groq(query)

            print(f"User said: {query}")
            print(f"Assistant: {response}")
            interrupted = speak(response)

            # Wait until the speech is finished or interrupted
            while speaker.Status.RunningState == 2:
                if keyboard.is_pressed('space'):
                    speaker.Speak("", 3)  # Stop speaking
                    print("Speech interrupted. Listening...")
                    interrupted = True
                    break
                time.sleep(0.1)

            # If not interrupted, add a small delay before listening again
            if not interrupted:
                time.sleep(1)

        except sr.UnknownValueError:
            speak("Sorry, I did not catch that.")
        except sr.RequestError as e:
            speak(f"Could not request results; {e}")

if __name__ == "__main__":
    voice_assistant()
 
