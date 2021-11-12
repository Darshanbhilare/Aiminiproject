import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import pyaudio
import time
from time import ctime
from tkinter import *
from PIL import ImageTk, Image

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


def takeCommand(ask=False):
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            speak(ask)
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


class Widget:
    def __init__(self):

        self.userText = None
        root = Tk()
        root.title('Robin GUI')
        root.geometry('950x360')
        img = ImageTk.PhotoImage(Image.open('robin2.jpg'))
        panel = Label(root, image=img)
        panel.pack(side='right', fill='both', expand='no')

        self.userText = StringVar()
        self.userText.set('Your Virtual Assistant')

        userFrame = LabelFrame(root, text='ROBIN🦋', font=('Comic sans ms', 24, 'bold'), fg='magenta')
        userFrame.pack(fill='both', expand='yes')

        top = Message(userFrame, textvariable=self.userText, bg='black', fg='white')
        top.config(font=("Comic sans ms", 15, 'italic'))
        top.pack(side='top', fill='both', expand='yes')
        btn = Button(root, text='Speak', font=('Arial', 10, 'bold'), bg='blue', fg='white',
                     command=self.clicked).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close', font=('Arial', 10, 'bold'), bg='red', fg='black',
                      command=root.destroy).pack(fill='x', expand='no')
        wishMe()
        root.mainloop()

    def clicked(self):
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            self.userText.set(results)
            print(results)
            speak(results)

        elif 'search' in query:
            search = takeCommand('What do you want to search for ?')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            speak('Here is what i found about' + search)

        if 'find location' in query:
            location = takeCommand('What is your location?')
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            speak('Here is location' + location)

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
            self.userText.set("Now playing: " + selected_file)
            print("Now playing: ", selected_file)
            os.startfile(os.path.join(music_dir, selected_file))

        elif 'shuffle music' in query:
            music_dir = 'C:\\Ai miniproject\\Test music'
            songs = os.listdir(music_dir)
            selected_file = random.choice(songs)
            self.userText.set("Now playing: " + selected_file)
            print("Now playing: ", selected_file)
            os.startfile(os.path.join(music_dir, selected_file))

        elif 'play video on artificial intelligence' in query:
            video_dir = 'C:\\Ai miniproject\\Test Video'
            videos = os.listdir(video_dir)
            print("Now playing: ", videos[0])
            self.userText.set("Now playing: " + videos[0])
            os.startfile(os.path.join(video_dir, videos[0]))

        elif 'time' in query:
            self.userText.set(f"Sir, the time is {ctime()}\n")
            speak("Sir the time is :" + ctime())
            print("Sir the time is :" + ctime())

        elif 'what day is it' in query:
            day = datetime.datetime.today().weekday() + 1
            Day_dict = {1: 'Monday', 2: 'Tuesday',
                        3: 'Wednesday', 4: 'Thursday',
                        5: 'Friday', 6: 'Saturday',
                        7: 'Sunday'}

            if day in Day_dict.keys():
                day_of_the_week = Day_dict[day]
                print(f"The day is {day_of_the_week}\n")
                self.userText.set(f"The day is {day_of_the_week}\n")
                speak(f"The day is {day_of_the_week}")

        elif 'weather report' in query:
            webbrowser.open("https://www.google.com/search?client=firefox-b-d&q=weather+report")
            self.userText.set(f"Sir, the current weather of your area is displayed on your screen")
            speak(f"Sir, the current weather of your area is displayed on your screen")

        elif 'open opera' in query:
            codePath = "C:\\Users\\yashk\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
            os.startfile(codePath)

        elif 'open calculator' in query:
            codePath = "C:\\Windows\\System32\\calc.exe"
            os.startfile(codePath)

        elif 'who are you' in query:
            self.userText.set("I'm ROBIN, an AI based smart voice assistant created by Yashvir and Vrutwic with the "
                              "help of python programming language. "
                              "I like to think I'm better than Alexa and Siri, but that's for you to decide")

            speak("I'm ROBIN, an AI based smart voice assistant created by "
                  "Yashvir and Vrutwic with the help of"
                  "python programming language. "
                  "I like to think I'm better than Alexa and Siri, but that's for you to decide.")

        elif 'change voice' in query:
            engine.setProperty('voice', voices[0].id)
            print('Changing the Voice....')
            speak("Hi I am JARVIS, other half of ROBIN, how can I assist you?")

        elif 'switch back to robin' in query:
            engine.setProperty('voice', voices[1].id)
            print('Changing the Voice....')
            speak("Hello its ROBIN again.")
            self.userText.set("Hello its ROBIN again.")

        elif 'send email to yash' in query:
            try:
                self.userText.set("What should I say?")
                speak("What should I say?")
                content = takeCommand()
                to = "yashkamble11@gmail.com"
                sendEmail(to, content)
                print("Your email has been sent\n")
                self.userText.set("Your email has been sent")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                self.userText.set("Sorry my friend. I am not able to send this email")
                speak("Sorry my friend. I am not able to send this email")
        elif 'goodbye' in query:
            print("Goodbye :) \n")
            self.userText.set("Goodbye :)")
            speak("Thank you sir, it was a pleasure assisting you. Have a nice day!")
            exit()

        else:
            print("Sorry, No functions found for that")
            speak("Sorry, No functions found for that")


if __name__ == '__main__':
    speak('Initializing Robin, Please Wait..')
    print('Initializing Robin, Please Wait..')
    time.sleep(1)
    widget = Widget()
