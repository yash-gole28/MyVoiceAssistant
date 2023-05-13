
import subprocess
import time
import pyttsx3 #used for converting text to speech
import requests  
import speech_recognition as sr  
import datetime
import wikipedia  
import webbrowser
import os #used to interract with the files
from bs4 import BeautifulSoup  #used to web scrapping and extract data from html amd xml documents
import pywhatkit
from jokes import *
import random
from latestNews import *
from stocks_price import *
from weather import *
from music import *
import wikipedia as googleScrap
import wolframalpha
import spacy
from pickups import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

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

    #speak("I am your personal assistant. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.dynamic_energy_threshold = True
        r.pause_threshold = 1
        r.energy_threshold = 4000
        r.operation_timeout = 5
        r.phrase_threshold = 0.3  # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
        r.non_speaking_duration = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        while Exception:
            speak("speak again")
            # speak("I didn't recognize what you said. Say that again please...")
            break
        return "None"
    return query

def ask_wolframalpha(question, app_id):
    client = wolframalpha.Client(app_id)
    try:
        res = client.query(question)
        answer = next(res.results).text
        return answer
    except:
        return "Sorry, I couldn't find an answer to that question."


if __name__ == "__main__":
    wishMe()
    while True:
        
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except:
                speak("NO such result found speak again")
                continue

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            speak("opening youtube")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
            speak("Opening google")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif "date" in query:
            today = datetime.date.today().strftime('%B %d, %Y')
            print("Today's date is:", today)
            speak("Today's date is: " + today)

        elif 'open code' in query:
            codePath = "C:\\Users\\YASH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)


        elif 'exit' in query or "quit" in query:
            speak("Thanks for giving me your time")
            quit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Yash.")

        elif 'joke' in query:
            speak(random.choice(funnyJokes))

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open(
                "https://www.google.nl/maps/place/"+ location)

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
        
        elif "shutdown" in query:
            subprocess.call("shutdown /s /t 1")

        elif "temperature in" in query:
            place = query.replace("current temperature in", "")

            search = "temperature in"
            url = f'https://www.google.com/search?q={search,place}'
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search}{place}  is {temp}")
            #speak(f"{place}  is {temp}")

        elif "google search" in query or "search" in query:
            
            google = query.replace("google search", "")
            sarch = google

            pywhatkit.search(sarch)

            try:
                result = googleScrap.summary(query, 2)

            except:
                speak("I didn't understand what you said ")

        elif "toss the coin" in query or "flip a coin" in query or"toss a coin" in query or "filp the coin" in query:
            num = 1
            flips = ["heads", "tails", "heads", "tails"]
            outcome = random.choice(flips)
            speak(f"it's{outcome}")
            print(outcome)

        elif "latest news" in query or "current news" in query:
            print(get_latest_news())
            speak(get_latest_news())

        elif "change voice" in query or "change the voice" in query or "change your voice" in query:
            engine.setProperty('voice', voices[1].id)
            speak("I am your female assistant , how may i help you?")

        elif "stock price" in query:
            symbol = input("Enter the stock symbol: ")
            result = get_stock_price(symbol)
            speak(result)
            print(result)

        elif "weather" in query:
            api_key ="7fee2fe4c9af84132d7ebea78943fdd9"
            speak("which city")
            city = takeCommand()
            speak(get_weather_info(api_key, city))
            print(get_weather_info(api_key, city))
        

        elif "speak slow" in query:
            engine.setProperty("rate",100)
            speak("hii i am your assistant")
        
        elif "speak fast" in query:
            engine.setProperty("rate",250)
            speak("hii i am your assistant")
        
        elif "speak normal" in query:
            engine.setProperty("rate",200)
            speak("ok boss")
        
        elif"open whatsapp"in query:
            webbrowser.open("https://web.whatsapp.com")

        elif "youtube search" in query:
            query = query.replace("youtube search","")
            youtube_search = query
            webbrowser.open("https://www.youtube.com/results?search_query="+ youtube_search)

        elif"play" in query:
            music_search = query.replace("play","")
            song_name= music_search
            speak("playing"+song_name)
            play_song(song_name)

        
        elif "tell me" in query:
            app_id = "UH355P-96YX36VGT8"
            
            leave = query.replace("tell me","")
            question = leave

            answer = ask_wolframalpha(question, app_id)

            print("Answer: ", answer)
            speak(ask_wolframalpha(question, app_id))

        
        elif "suggest" in query:
            speak('what')
            nlp = spacy.load("en_core_web_sm")

            api_key = "03641fcd658a4f91543faf02a10df7fa"

            genre = takeCommand()
            command = genre
            doc = nlp(command)
            for ent in doc.ents:
                if ent.label_ == "":
                 genre = ent.text.lower()

            if genre:
                url = f"http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag={genre}&api_key={api_key}&format=json"
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    tracks = data["tracks"]["track"]
                    if tracks:
                        print(f"Here are some song suggestions for {genre}:")
                        for track in tracks[:10]:
                            name = track["name"]
                            artist = track["artist"]["name"]
                            print(f"{name} - {artist}")
                    else:
                        print(f"No song suggestions found for {genre}.")
                else:
                    print("Error: Unable to retrieve data")
            else:
                print("No music genre detected in the command.")

        
        elif "pick up line" in query or "pickup line" in query:
            speak(random.choice(pickupLines))

        elif "what tasks can you perform" in query or "what else can you do" in query or "what can you do" in query :
            speak("I'm still learning, if you ask me I can tell you the weather report for any location, keep you up to date with the latest news, play any songs you request, flip a coin,provide you current time, and even perform a Google search for anything you need to know. ")

        elif "how will you assist me" in query or "how will you help me" in query:
            speak("I will try my best to perform tasks you assign me")
        
        