from PyDictionary import PyDictionary
from GoogleNews import GoogleNews
import pyowm
googlenews = GoogleNews()
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import datetime
import wikipedia
import time
import smtplib
import keyboard as k
import pyautogui
import pyjokes
import psutil
from sys import platform

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def main2():
    query = takeCommand().lower()
    if query.count(wake) > 0:
        os.startfile('C:\\Program Files\\Rainmeter\\Rainmeter.exe')
        speak('I am ready')
        wishMe()
        query = takeCommand().lower()
        if "hello" in query:
            speak("Hello sir")
        elif "edit" in query:
            speak("Sir I am EDITH,My actual name is Even Dead I am the hero")
        elif "what can you do" in query:
            speak("I can send emails, search things in wikipedia, open apps and open websites")
        elif "weather" in query:
            owm = pyowm.OWM('21af4d40372f3029b260e9c76cddfcc7')  # You MUST provide a valid API key

            # Search for current weather in London (Great Britain)
            observation = owm.weather_at_place('Mumbai,India')
            w = observation.get_weather()
            speak('Current speed of wind is' + str(w.get_wind()['speed']))
            speak('Current Humidity is ' + str(w.get_humidity()))
            b = w.get_temperature('celsius')
            speak('Current temperature is' + str(b['temp']) + 'degree celsius')
        elif "thank you" in query:
            speak("Most welcome sir")
        elif 'your code ' in query:
            codePath = "C:\\Users\\HP\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open word' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Word 2010"
            os.startfile(codePath)
        elif "solve expression" in query:
            speak("Enter a expression")
            calc = input("Enter a expression: ")
            print("Answer is " + str(eval(calc)))
            speak("Answer is " + str(eval(calc)))
        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()
        elif 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[1].id)
            else:
                engine.setProperty('voice', voices[0].id)
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/?gws_rd=ssl")
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/?gl=IN")
        elif 'search youtube' in query:
            speak('Searching Youtube...')
            query = query.replace("search youtube for", "")
            url = 'https://www.youtube.com/results?search_query=' + str(query)
            webbrowser.open_new(url)
        elif 'java' in query:
            codePath = "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\BlueJ\\BlueJ"
            os.startfile(codePath)
        elif 'open power point' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft PowerPoint 2010"
            os.startfile(codePath)
        elif 'open excel' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Excel 2010"
            os.startfile(codePath)
        elif 'cpu' in query:
            cpu()
        elif 'give me news of' in query:
            query = query.replace("give me news of", "")
            googlenews = GoogleNews('en')
            googlenews.search(query)
            speak('Following are headlines for news you asked me')
            for i in range(10):
                speak(str(googlenews.gettext()[i]))
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'joke' in query:
            joke()
        elif 'what is time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'play music one' in query:
            music_dir = 'D:\\data d\\Non Critical\\songs'
            songs = os.listdir(music_dir)

            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'play music 2' in query:
            music_dir = 'D:\\data d\\Non Critical\\songs'
            songs = os.listdir(music_dir)

            os.startfile(os.path.join(music_dir, songs[1]))
        elif 'play music 3' in query:
            music_dir = 'D:\\data d\\Non Critical\\songs'
            songs = os.listdir(music_dir)

            os.startfile(os.path.join(music_dir, songs[2]))
        elif "repeat song 1" in query:
            music_dir = 'D:\\data d\\Non Critical\\songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "repeat song 2" in query:
            music_dir = 'D:\\data d\\Non Critical\\songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[1]))
        elif 'shutdown' in query:
            if platform == "win32":
                os.system('shutdown /p /f')
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('poweroff')
        elif 'your name' in query:
            speak('My name is JARVIS')
        elif 'stands for' in query:
            speak('J.A.R.V.I.S stands for JUST A RATHER VERY INTELLIGENT SYSTEM')
        elif 'repeat song 3' in query:
            music_dir = 'D:\\data d\\Non Critical\\songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[2]))
        elif 'according to google' in query:
            speak("Here is search result")
            query = query.replace("according to google", "")
            url = "https://www.google.co.in/search?q=" + (str(query)) + "&oq=" + (str(
                query)) + "&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
            webbrowser.open_new(url)
        elif 'email to me' in query:

            try:
                speak("What should I write?")

                content = takeCommand()
                to = 'dakshdesai54@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent sir!")
            except Exception as e:
                print(e)
                speak("Sorry sir,I am unable to send email")
        elif 'email to mom' in query:

            try:
                speak("What should I say?")

                content = takeCommand()
                to = 'hadesai1979@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent sir!")
            except Exception as e:
                print(e)
                speak("Sorry sir,I am unable to send email")
        elif 'email to manan' in query:

            try:
                speak("What should I say?")

                content = takeCommand()
                to = 'ardumanan@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent sir!")
            except Exception as e:
                print(e)
                speak("Sorry sir,I am unable to send email")
        elif 'email to dad' in query:

            try:
                speak("What should I say?")

                content = takeCommand()
                to = 'amitdes@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent sir!")
            except Exception as e:
                print(e)
                speak("Sorry sir,I am unable to send email")
        elif 'location' in query:
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.open_new_tab(url)
            speak('Here is the location ' + location)
        elif 'remember that' in query:
            speak("what should i remember sir")
            rememberMessage = takeCommand()
            speak("you said me to remember" + rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()
        elif 'sleep' or 'Sleep' in query:
            os.system('TASKKILL /F /IM Rainmeter.exe')
            main2()
        elif 'dictionary' in query:
            speak('What you want to search in your intelligent dictionary?')
            dictionary = PyDictionary()
            speak(dictionary.meaning(takeCommand()))
        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())
        elif 'your master' in query:
            speak('Owner of DakshIndustries is my master,Mister Daksh')
        elif 'email to unknown' in query:
            z = input("Sir please enter email ID of reciver: ")
            speak("Sir please enter email ID of reciver")
            try:
                speak("What should I say?")

                content = takeCommand()
                to = z
                sendEmail(to, content)
                speak("Email has been sent sir!")
            except Exception as e:
                print(e)
                speak("Sorry sir,I am unable to send email")
        elif "send data" in query:

            senddir = input('Enter directory to send files: ')
            codePath = "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Windows PowerShell\\Windows PowerShell"
            os.startfile(codePath)
            time.sleep(2)
            k.write("cd " + senddir)
            k.press_and_release('enter')
            time.sleep(0.5)
            k.write('py -m http.server 8000')
            k.press_and_release('enter')

        elif "send my D drive" in query:
            codePath = "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Windows PowerShell\\Windows PowerShell"
            os.startfile(codePath)
            time.sleep(2)
            k.write("cd D:\\")
            k.press_and_release('enter')
            time.sleep(0.5)
            k.write('py -m http.server 8000')
            k.press_and_release('enter')
        elif "send my python code" in query:
            codePath = "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Windows PowerShell\\Windows PowerShell"
            os.startfile(codePath)
            time.sleep(2)
            k.write("cd C:\\Users\\HP\\Desktop\\PythonCodes")
            k.press_and_release('enter')
            time.sleep(0.5)
            k.write('py -m http.server 8000')
            k.press_and_release('enter')
        elif "send my machine learning project" in query:
            codePath = "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Windows PowerShell\\Windows PowerShell"
            os.startfile(codePath)
            time.sleep(2)
            k.write("cd C:\\Users\\HP\\Desktop\\MachineLearning")
            k.press_and_release('enter')
            time.sleep(0.5)
            k.write('py -m http.server 8000')
            k.press_and_release('enter')
        elif "send my tally data" in query:
            codePath = "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Windows PowerShell\\Windows PowerShell"
            os.startfile(codePath)
            time.sleep(2)
            k.write("cd C:\\Users\\HP\\Desktop\\NMSHAHOFFICE")
            k.press_and_release('enter')
            time.sleep(0.5)
            k.write('py -m http.server 8000')
            k.press_and_release('enter')
        elif "send my download" in query:
            codePath = "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Windows PowerShell\\Windows PowerShell"
            os.startfile(codePath)
            time.sleep(2)
            k.write("cd Downloads")
            k.press_and_release('enter')
            time.sleep(0.5)
            k.write('py -m http.server 8000')
            k.press_and_release('enter')
        elif "send my screenshot" in query:
            codePath = "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Windows PowerShell\\Windows PowerShell"
            os.startfile(codePath)
            time.sleep(2)
            k.write("cd C:\\Users\\HP\\Videos\\Captures")
            k.press_and_release('enter')
            time.sleep(0.5)
            k.write('py -m http.server 8000')
            k.press_and_release('enter')
        elif "send my photo" in query:
            codePath = "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Windows PowerShell\\Windows PowerShell"
            os.startfile(codePath)
            time.sleep(2)
            k.write("cd Pictures")
            k.press_and_release('enter')
            time.sleep(0.5)
            k.write('py -m http.server 8000')
            k.press_and_release('enter')
        elif "send my document" in query:
            codePath = "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Windows PowerShell\\Windows PowerShell"
            os.startfile(codePath)
            time.sleep(2)
            k.write("cd Documents")
            k.press_and_release('enter')
            time.sleep(0.5)
            k.write('py -m http.server 8000')
            k.press_and_release('enter')
        elif "open video downloader" in query:
            codePath = "D:\\YoutubeVideoDownloader\\YoutubeVideoDownloader - Shortcut"
            os.startfile(codePath)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Welcome sir")
    speak('Sir let me give you current weather forecast')
    owm = pyowm.OWM('21af4d40372f3029b260e9c76cddfcc7')  # You MUST provide a valid API key

    # Search for current weather in London (Great Britain)
    observation = owm.weather_at_place('Mumbai,India')
    w = observation.get_weather()
    speak('Current speed of wind is' + str(w.get_wind()['speed']))
    speak('Current Humidity is ' + str(w.get_humidity()))
    b = w.get_temperature('celsius')
    speak('Current temperature is' + str(b['temp']) + 'degree celsius')


def takeCommand():
    # It takes microphone input from the user and returns string output

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


def joke():
    for i in range(5):
        speak(pyjokes.get_jokes()[i])


def screenshot():
    img = pyautogui.screenshot()

    img.save('C:\\Users\\HP\\Pictures\\Saved Pictures\\screenshot.png')


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('dakshdesai54@gmail.com', 'Qasdf@123')
    server.sendmail('dakshdesai54@gmail.com', to, content)
    server.close()


wake = 'wake up'

while True:
    main2()
