import smtplib
import wikipedia
import speech_recognition as sr
import pyttsx3
import time
from time import ctime
import webbrowser
import playsound
import os
import random
import datetime
from gtts import gTTS
from tkinter import *
from PIL import ImageTk, Image

r = sr.Recognizer()
speaker = pyttsx3.init()


def record_audio(ask=False):  # user voice record
    with sr.Microphone() as source:
        if ask:
            rob_voice(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print('User said :' + voice_data)
        except Exception:
            print('Oops something went Wrong')
            # lee_voice('Oops something went Wrong')
        return voice_data


def rob_voice(audio_string):  # Play audio text to voice
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        rob_voice("Good Morning!")
    elif hour >= 12 and hour < 18:
        rob_voice("Good Afternoon!")
    else:
        rob_voice("Good Evening!")
    print("I am Robin sir. Please tell me how may I help you?")
    rob_voice("I am Robin sir. Please tell me how may I help you")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bkdevil1999@gmail.com', 'BkDevil@1999')
    server.sendmail('bkdevil1999@gmail.com', to, content)
    server.close()


class Widget:  # GUI OF VIRTUAL ASSISTANT AND COMMANDS GIVEN
    def __init__(self):
        root = Tk()
        root.title('Robin GUI')
        root.geometry('950x360')
        img = ImageTk.PhotoImage(Image.open('robin2.jpg'))
        panel = Label(root, image=img)
        panel.pack(side='right', fill='both', expand='no')
        #compText = StringVar()
        userText = StringVar()
        userText.set('Your Virtual Assistant')
        userFrame = LabelFrame(root, text='ROBIN🦋', font=('Comic sans ms', 24, 'bold'), fg='magenta')
        userFrame.pack(fill='both', expand='yes')
        top = Message(userFrame, textvariable=userText, bg='black', fg='white')
        top.config(font=("Comic sans ms", 15, 'bold'))
        top.pack(side='top', fill='both', expand='yes')
        # compFrame = LabelFrame(root, text="Lena", font=('Railways', 10, 'bold'))
        # compFrame.pack(fill="both", expand='yes')
        btn = Button(root, text='Speak', font=('arial', 10, 'bold'), bg='blue', fg='white',
                     command=self.clicked).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close', font=('arial', 10, 'bold'), bg='red', fg='black',
                      command=root.destroy).pack(fill='x', expand='no')
        wishMe()
        root.mainloop()

    def clicked(self):
        print("Listening...")
        voice_data = record_audio()
        voice_data = voice_data.lower()
        if 'search' in voice_data:
            search = record_audio('What do you want to search for ?')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            rob_voice('Here is what i found about' + search)
        if 'find location' in voice_data:
            location = record_audio('What is your location?')
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            rob_voice('Here is location' + location)

        elif 'what is the time' in voice_data:
            rob_voice("Sir the time is :" + ctime())

        elif 'search in wikipedia' in voice_data:
            rob_voice('Searching Wikipedia...')
            voice_data = voice_data.replace("wikipedia", "")
            results = wikipedia.summary(voice_data, sentences=2)
            rob_voice("According to Wikipedia")
            print(results)
            rob_voice(results)

        elif 'open youtube' in voice_data:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in voice_data:
            webbrowser.open("https://www.google.com/")

        elif 'open stack overflow' in voice_data:
            webbrowser.open("https://stackoverflow.com/")

        elif 'open vidyalankar website' in voice_data:
            webbrowser.open("https://vsit.edu.in/")

        elif 'play music' in voice_data:
            music_dir = 'C:\\Ai miniproject\\Test music'
            songs = os.listdir(music_dir)
            selected_file = random.choice(songs)
            print("Now playing: ", selected_file)
            os.startfile(os.path.join(music_dir, selected_file))

        elif 'play video on artificial intelligence' in voice_data:
            video_dir = 'C:\\Ai miniproject\\Test Video'
            videos = os.listdir(video_dir)
            print("Now playing: ", videos[0])
            os.startfile(os.path.join(video_dir, videos[0]))

        elif 'what day is it' in voice_data:
            day = datetime.datetime.today().weekday() + 1
            Day_dict = {1: 'Monday', 2: 'Tuesday',
                        3: 'Wednesday', 4: 'Thursday',
                        5: 'Friday', 6: 'Saturday',
                        7: 'Sunday'}

            if day in Day_dict.keys():
                day_of_the_week = Day_dict[day]
                rob_voice(f"The day is {day_of_the_week}")
                print(f"The day is {day_of_the_week}\n")
                #self.userText.set(f"The day is {day_of_the_week}\n")

        elif 'weather report' in voice_data:
            webbrowser.open("https://www.google.com/search?client=firefox-b-d&q=weather+report")
            rob_voice(f"The current weather of your area is displayed on your screen")

        elif 'open opera' in voice_data:
            codePath = "C:\\Users\\yashk\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
            os.startfile(codePath)

        elif 'open calculator' in voice_data:
            codePath = "C:\\Windows\\System32\\calc.exe"
            os.startfile(codePath)

        elif 'who are you' in voice_data:
            rob_voice("I'm ROBIN, an AI based smart voice assistant created by "
                      "Yashvir and Vrutwik with the help of python programing language. "
                      "I like to think I'm better than Alexa and Siri, but that's for you to decide.")

        elif 'send email to yash' in voice_data:
            try:
                rob_voice("What should I say?")
                content = record_audio()
                to = "yashkamble11@gmail.com"
                sendEmail(to, content)
                print("Your email has been sent\n")
                rob_voice("Email has been sent!")
            except Exception as e:
                print(e)
                rob_voice("Sorry my friend. I am not able to send this email")

        if 'Goodbye' in voice_data:
            rob_voice('Thanks have a good day ')
            exit()


if __name__ == '__main__':
    widget = Widget()

time.sleep(1)
while 1:
    voice_data = record_audio()
    widget.clicked()

speaker.runAndWait()