import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
#from ecapture import ecapture as ec
import wolframalpha
import json
import requests


print('Loading your voice assistant')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, good morning")
        print("Hello, good morning")
    elif hour >= 12 and hour < 18:
        speak("Hello, good afternoon")
        print("Hello, good afternoon")
    else:
        speak("Hello, good evening")
        print("Hello, good evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"User said: {statement}\n")

        except Exception as e:
            speak("Sorry I can't hear you, can you say that again ?")
            return "None"
        return statement


speak("Loading your voice assistant")
wishMe()





#if __name__=='__main__':
def MainFucntion():
    while True:
        speak("How can I help you ?")
        statement = takeCommand().lower()
        if statement == 0:
            continue
        

        if "shutdown" in statement or "goodbye" in statement or "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('Your personal assistant is shutting down, good bye!')
            print('your personal assistant is shutting down, good bye!')
            exit()

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            break

        elif 'hello' in statement:
            speak('Hello, nice to meet you :D')
            print('Hello, nice to meet you :D')
            break

        elif 'youtube' in statement or 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            print("Youtube is opening now")
            speak("Youtube is opening now")
            break

        elif 'goole' in statement or 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            print("Google is opening now")
            speak("Google is opening now")
            break

        elif 'gmail' in statement or 'open gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            print("Google mail is opening now")
            speak("Google mail is opening now")
            break
        
        elif 'hey' in statement or 'hey robot' in statement:
            speak("What do you want from this robot")
            print("What do you want from this robot")
            statement = takeCommand()
            SimsimiKey = "40fP0WWcctMh-AEE6cu8vUyXsZiFzN3eR9sWXpmn"
            url="https://wsapi.simsimi.com/190410/talk"
            payload ="{\n\t\"utext\": \""+ statement +"\", \n\t\"lang\": \"en\" \n}"
            headers = {
                'Content-Type': "application/json",
                'x-api-key': "40fP0WWcctMh-AEE6cu8vUyXsZiFzN3eR9sWXpmn"
            }
            response = requests.request("POST", url, data=payload, headers=headers)
            response = json.loads(response.text)
            print("robot reply: " + response["atext"])
            speak("robot reply: " + response["atext"])
            break

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name ?")
            city_name = takeCommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                print("City not found")
                speak("City Not Found ")

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")
            break

        elif 'who are you' in statement or 'what can you do' in statement:
            print('I am your voice assistant, programmed to answer some simple task like show time, open map, weather forecast,etc.')
            speak('I am your voice assistant, programmed to answer some simple task like show time, open map, weather forecast,etc.')
            break

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was made by Duong and Khanh")
            print("I was made by Duong and Khanh")
            break

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            print('Here is stackoverflow')
            speak("Here is stackoverflow")
            break

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://dantri.com.vn/")
            print('Here are the news from dantri news, hope you have a good time reading.')
            speak('Here are the news from dantri news, hope you have a good time reading.')
            break

        elif 'search' in statement:
            speak("What do you want to search for ?")
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            print("Here is your result !")
            break

        elif 'your name' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
            break

time.sleep(5)
