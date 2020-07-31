import datetime
import os
import smtplib
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia

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

def google():
    speak("Opening Google...")
    webbrowser.open('https://www.google.com/')

if __name__ == '__main__':
    wishMe()
    if 1:
        query = takeCommand().lower()

        # Logicfor executing tasks based on query
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