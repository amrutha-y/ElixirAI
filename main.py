import win32com.client
import speech_recognition as sr
import os


speaker = win32com.client.Dispatch("SAPI.SpVoice")

#while 1:aa
 #   print("ENTER SOME TEXT")
  #  s = input()
   # speaker.Speak(s)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"


if __name__ == '__main__':
    print('Elixir A.I')
    speaker.Speak("Welcome to Elixir A I")
    while True:
        print("Listening...")
        query = takeCommand()
        speaker.Speak(query)