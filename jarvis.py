import datetime
import os
import time
import smtplib
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import sys
import requests
import json
import subprocess
import pywhatkit as kit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning!!")
    elif hour >=12 and hour <=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")

    speak("I am Jarvis, Your personal assistant sir. How may i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() == source :
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    # with sr.WavFile("test.wav") as source:  # use "test.wav" as the audio source
    #     audio = r.record(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)
    except Exception as e:
        # print(e)
        print("Couldn't recognize! Kindly speak again")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mananbedilps@gmail.com', passwordFile)
    server.sendmail('mananbedilps@gmail.com', to, content)
    server.close()



if __name__ == '__main__':
    wishMe()
    if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com/')

        elif 'open google' in query:
            webbrowser.open('https://www.google.com/')

        elif 'open my github account' in query:
            webbrowser.open('https://github.com/manan-bedi2908')

        elif 'open my linkedin account' in query:
            webbrowser.open('')

        elif 'play music' in query:
            music_dir = 'E:\\SONGS'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {time}")

        elif 'open sublime text editor' in query:
            loc = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(loc)

        elif 'ip network settings' in query:
            os.ipconfig()

        elif 'create a new directory' in query:
            try:
                speak("Creating Directory")
                directory = "GeeksForGeeks"

                # Parent Directory path
                parent_dir = "E:\\HTML FILE"

                # Path
                path = os.path.join(parent_dir, directory)

                # Create the directory
                # 'GeeksForGeeks' in
                # '/home / User / Documents'
                os.mkdir(path)
            except:
                speak("Error occured!!")

        elif 'send email to manan' in query:
            try:
                speak("What should i send?")
                content = takeCommand()
                to = "mananbedilps@gmail.com"
                sendEmail(to, content)
                speak("E-Mail delivered!!")
            except Exception as e:
                print("Error Occured")
                speak("Sorry, I wasn't able to send the email")

        elif "weather" in query:
            api_key = "41fa3f5489msh283ac1b29e9fbe6p105715jsnff18271a9177"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("Getting your city from IPStack API")
            send_url = "http://api.ipstack.com/check?access_key=97ca076f0f857bd3105915b238a61bf2"
            geo_req = requests.get(send_url)
            geo_json = json.loads(geo_req.text)
            latitude = geo_json['latitude']
            longitude = geo_json['longitude']
            city = geo_json['city']
            speak("You are in {}".format(city))
            url = base_url + "appid="+api_key+"&q="+city
            response = requests.get(url)
            loc = response.json()
            if loc['cod']!="404":
                y = loc["main"]
                current_temp = y["temp"]
                current_humidity = y["humidity"]
                z = loc["weather"]
                weather_desc = z[0]['description']
                speak("Temperature in Kelvin unit is" + str(current_temp) + "and humidity is" + str(current_humidity) + "And description" + str(weather_desc))
                print("Temperature in Kelvin unit is" + str(current_temp) + "and humidity is" + str(current_humidity) + "And description" + str(weather_desc))
            else:
                speak("City not found")
                print("City not found")

        elif "search" in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)

        elif "log off" in query or "shutdown" in query:
            speak("Turning off the computer")
            subprocess.call(["shutdown", "/l"])

        elif "set an alarm" in query:
            now = datetime.datetime.now()
            alarm_time = datetime.datetime.combine(now.date(), datetime.time(18, 0, 0))
            time.sleep((alarm_time - now).total_seconds())
            os.system("ALL RISE.mp3")

        elif "send whatsapp message" in query:
            speak("Enter the Phone Number of the person whom you want to send the message")
            inp = input("Enter WhatsApp Number")
            kit.sendwhatmsg(inp, "Hello Friend! How are You?", 18, 21)

        elif 'quit' in query:
            sys.exit()