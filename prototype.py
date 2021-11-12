import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


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
    print("I am Robin sir. Please tell me how may I help you?")
    speak("I am Robin sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bkdevil1999@gmail.com', 'BkDevil@1999')
    server.sendmail('bkdevil1999@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'search' in query:
            query = query.replace("search for", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com/")

        elif 'open vidyalankar website' in query:
            webbrowser.open("https://vsit.edu.in/")


        elif 'play music' in query:
            music_dir = 'C:\\Ai miniproject\\Test music'
            songs = os.listdir(music_dir)
            selected_file = random.choice(songs)
            print("Now playing: ", selected_file)
            os.startfile(os.path.join(music_dir, selected_file))

        elif 'play video on artificial intelligence' in query:
            video_dir = 'C:\\Ai miniproject\\Test Video'
            videos = os.listdir(video_dir)
            print("Now playing: ", videos[0])
            os.startfile(os.path.join(video_dir, videos[0]))

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}\n")

        elif 'weather report' in query:
            webbrowser.open("https://www.google.com/search?client=firefox-b-d&q=weather+report")
            speak(f"Sir, the current weather of your area is displayed on your screen")

        elif 'open opera' in query:
            codePath = "C:\\Users\\yashk\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
            os.startfile(codePath)

        elif 'open cal' in query:
            codePath = "C:\\Windows\\System32\\calc.exe"
            os.startfile(codePath)

        elif 'who are you' in query:
            speak("I'm Robin, an AI based smart voice assistant created by Yashveer and Vrutwic with the help of "
                  "python programming language. "
                  "I like to think I'm better than Alexa and Siri, but that's for you to decide.")

        elif 'send email to yash' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yashkamble11@gmail.com"
                sendEmail(to, content)
                print("Your email has been sent\n")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")

        elif 'goodbye' in query:
            print("Goodbye :) \n")
            speak("Thank you sir, it was a pleasure assisting you. Have a nice day!")
            exit()
