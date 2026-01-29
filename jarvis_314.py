##use for run the program - python jarvis_314.py
import datetime
import wikipedia
import webbrowser
import os
import pyttsx3
import win32com.client

# Text to speech
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Wish user
def wishMe():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis. How can I help you")

# Windows SAPI microphone input
def takeCommand():
    query = input("Type your command here: ").lower()
    return query

    recognizer = win32com.client.Dispatch("SAPI.SpSharedRecognizer")
    context = recognizer.CreateRecoContext()
    grammar = context.CreateGrammar()
    grammar.DictationSetState(1)

    print("Listening...")
    event = context.WaitForNotifyEvent(10000)
    result = context.Recognize()

    if result:
        text = result.PhraseInfo.GetText()
        print("You said:", text)
        return text.lower()
    return ""

# Main program
if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand()

        if not query:
            continue

        if "wikipedia" in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)

        elif "open youtube" in query:
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            webbrowser.open("https://google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("https://stackoverflow.com")

        elif "play music" in query:
            music_dir = "D:\\Music"   # change if needed
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        elif "open code" in query:
            codePath = r"C:\Users\YourUserName\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif "exit" in query or "quit" in query:
            speak("Goodbye")
            break
