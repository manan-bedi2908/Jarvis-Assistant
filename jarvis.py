import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
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

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logicfor executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia, ")
            speak(results)

