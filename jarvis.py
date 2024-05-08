import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')  # getting details of current voice
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis here. Please tell me how may I help you")

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.
    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shreysamal101@gmail.com', 'Payal@123')
    server.sendmail('shreysamal101@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()  # Converting user query into lower case
        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\SHREYA\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif 'email to shri' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "shreysamal101@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry shri. I am not able to send this email")

