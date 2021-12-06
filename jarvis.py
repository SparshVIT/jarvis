import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)
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
    speak("Hii i am Jarvis sir. Please tell me how may i help you")
def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ",query)
    except Exception as e:
       # print(e)
        print("Say that again please")
        return "None"
    return query

if __name__ == "__main__":
    #speak("Hello Sparsh!")
    wishMe()
    query=takeCommand().lower()

    if 'wikipedia' in query:
        speak("Searching....")
        query=query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        speak("Acording to wikipedia")
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'play music' in query:
        webbrowser.open("gaana.com")
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(strTime)
    elif 'open vs' in query:
        codepath="C:\Users\hp\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        os.startfile(codepath)
    
            
        
        
        
                                                  
        
