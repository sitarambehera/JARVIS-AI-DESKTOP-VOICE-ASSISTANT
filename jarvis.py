import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    
   
    else:
        speak("Good Evening!")
    
    speak("Hello sir I am Jarvis . how can i help you sir!")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......  ")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.......") 
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        
        print("say that again please.....")
        return "None"

    return(query)
    

if __name__ == "__main__":
    wishMe()

    while(True):
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching Wikipedia......')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open spotify' in query:
            webbrowser.open("spotify.com")

    

        elif 'play movies' in query:
            movies_dir = 'E:\\Movies\\Hollywood'
            movies = os.listdir(movies_dir)
            print(movies)
            os.startfile(os.path.join(movies_dir,movies[7]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir , the time is {strTime}")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

    
    