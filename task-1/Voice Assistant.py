import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os

# Initialize speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # choose voice 0 or 1

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice command and convert to text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("🔎 Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"🗣️ You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I could not understand. Please repeat.")
        return ""
    except sr.RequestError:
        speak("Network error. Please check your connection.")
        return ""

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your voice assistant. How may I help you?")

def run_assistant():
    wish_me()
    while True:
        query = listen()

        if "wikipedia" in query:
            import wikipedia
            try:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "").strip()
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                speak("Sorry, I could not find results.")

        elif "open youtube" in query:
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            webbrowser.open("https://google.com")

        elif "time" in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"⌚ Current Time: {str_time}")   # also print to console
            speak(f"The time is {str_time}")
            
        elif "date" in query:
            str_date = datetime.datetime.now().strftime("%d %B %Y")
            print(f"📅 Today's Date: {str_date}")
            speak(f"Today's date is {str_date}")

        elif "open code" in query:
            path = r"C:\Users\DELL\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(path)

        elif "exit" in query or "quit" in query:
            speak("Goodbye! Have a nice day.")
            break

if __name__ == "__main__":
    run_assistant()
