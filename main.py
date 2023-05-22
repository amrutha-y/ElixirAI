import win32com.client
import speech_recognition as sr
import os
import webbrowser
import openai
import datetime

speaker = win32com.client.Dispatch("SAPI.SpVoice")

#while 1:
 #   print("ENTER SOME TEXT")
  #  s = input()
   # speaker.Speak(s)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Elixir"


if __name__ == '__main__':
    print('Elixir A.I')
    speaker.Speak("Welcome to Elixir A I")
    while True:
        print("Listening...")
        query = takeCommand()
        #speaker.Speak(query)
        #Add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {site[0]} ")
                webbrowser.open(site[1])
                
        if "open vs code" in query:
            #vscodePath = "code ."
            os.system(f"code .")
            
        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speaker.Speak(f"Time is {hour} past {min} minutes")