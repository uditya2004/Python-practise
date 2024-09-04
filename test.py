import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening...")
    recognizer.adjust_for_ambient_noise(source)
    try:
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"Recognized: {text}")
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except Exception as e:
        print(f"Error: {e}")
