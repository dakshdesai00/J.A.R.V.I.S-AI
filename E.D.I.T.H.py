import pyttsx3 
import speech_recognition as sr 
import datetime
import webbrowser
import os 
import datetime
import wikipedia
import time
import smtplib
from pathlib import Path

txt = Path('D:\\Non Critical\\jarvisdata.txt').read_text()
txt = txt.replace('\n', '')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am EDITH,I have all access to DakshIndustries")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to your command sir...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Sir said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('dakshdesai54@gmail.com', txt)
    server.sendmail('dakshdesai54@gmail.com', to, content)
    server.close() 

if __name__ == "__main__":
    wishMe() 
    while True:   
        query = takeCommand().lower()
        if "code" in query:
            codePath = "put path of visual studio code"
            os.startfile(codePath)   
        elif "scratch" in query:
            codePath = "put path of scratch"
            os.startfile(codePath)     
        elif 'whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/") 
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=5) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'what is time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'play music one' in query:
            music_dir = 'D:\\Non Critical\\songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'play music 2' in query:
            music_dir = 'D:\\Non Critical\\songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[1]))
        elif 'play music 3' in query:
            music_dir = 'D:\\Non Critical\\songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[2]))    