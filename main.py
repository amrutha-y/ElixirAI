import win32com.client
import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
from config import apikey

speaker = win32com.client.Dispatch("SAPI.SpVoice")

chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Amrutha: {query}\n Elixir: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    speaker.Speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI responded for Prompt: {prompt} \n\n\n"
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
	)
    
    text = text+response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")


    with open(f"Openai/{''.join(prompt.split('openai')[1:]).strip() }.txt", "w") as f:
        f.write(text)
    

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
            
        elif "Using open a i".lower() in query.lower():
            ai(prompt=query)
            
        elif "quit".lower() in query.lower():
            exit()
            
        elif "reset".lower() in query.lower():
            charStr = ""
            
        else:
            print("chatting")
            chat(query)
            
        
    
		