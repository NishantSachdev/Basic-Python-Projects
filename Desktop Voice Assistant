import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    else :
        speak("Good Evening!")
    speak(" I am siri, how may i help you")

def takeCommand():        # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') # Using google for voice recognition.
        print(f"User said: {query}\n")      # User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   # Say that again will be printed in case of improper voice 
        return "None"                       # None string will be returned
    return query


if __name__ == "__main__":
    speak("Hello Sir")
    wishme()
    while True:
        query = takeCommand().lower()

        # DIFFERENT TASKS #
        
        # ** Open Websites ** #
        # YouTube
        if "open youtube" in query:
            webbrowser.open("youtube.com")
        # Google
        elif "open google" in query:
            webbrowser.open("google.com")
        # W3schools
        elif "open w3schools" in query:
            webbrowser.open("w3schools.com")

        # Date & Time
        elif "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")
        elif "date" in query:
            date=datetime.datetime.now().strftime("%A:%d:%B:%Y")
            speak(f"The date is {date}")
        
        # Wikipedia
        elif "wikipedia" in query :
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        # Open Files in PC
        elif "open database cheat sheet" in query:
            Path1 = "C:\\Users\\Admin\\Desktop\\SQL\\MySQLCheatsheet.pdf"
            os.startfile(Path1)
        elif "open python cheat sheet" in query:
            Path2 = "C:\\Users\\Admin\\Desktop\\Python Course with Notes\\Python_Cheatsheet.pdf"
            os.startfile(Path2)
        elif "open steam" in query:
            Path3 = "I:\\NISHANT\\STEAM\\steam"
            os.startfile(Path3)
        elif "open chrome" in query:
            Path4 = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome"
            os.startfile(Path4)
        elif ("open work bench" or "open workbench") in query:
            Path5 = "C:\\Program Files\\MySQL\\MySQL Workbench 8.0\\MySQLWorkbench"
            os.startfile(Path5)
        
        # Quit
        elif "exit" in query:
            exit()
