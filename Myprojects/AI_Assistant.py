import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
import datetime
import smtplib
from config import apikey
import openai
from googlesearch import search
engine=pyttsx3.init() #engine is an object
voices=engine.getProperty('voices')
voices=engine.setProperty('voice',voices[1].id)
volume=engine.getProperty('volume')
print(volume)
rate=engine.getProperty('rate')
print(rate)
rate=engine.setProperty('rate',165)
engine.setProperty('volume',1.0)
def speech(audio):
    engine.say(audio)
    engine.runAndWait()
def wish_me():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speech("Good Morning Master")
    elif hour>=12 and hour<18:
        speech("Good Afternoon Master")
    else:
        speech("Good Evening Master")

def take_command():
    r=sr.Recognizer()
    m=sr.Microphone()
    #print(sr.Microphone.list_microphone_names())
    m=sr.Microphone(device_index=1)
    with m as source:
        print("Listening...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        # You can capture input from the microphone using the listen() method of the Recognizer class inside of the with block. This method takes an audio source as its first argument and records input from the source until silence is detected.
        query=None
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User Said {query}\n")
    except Exception as e:
        print(e)
        print("Please Say That Again Please")
        return "None"
        
    return query
def openaifunc(msg):
    openai.api_key = apikey
    text=f"The Open AI Result generated for {msg} is: \n"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": msg
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    speech("Fetching Results from Chat GPT-3.5 Turbo")
    try:
        openai_results=response["choices"][0]["message"]["content"]
        if not os.path.exists("openai"):
            os.mkdir("openai")
        with open(f"Myprojects/openai/{msg[0:30]}.txt",'w') as f:
            f.write(text+openai_results)
        print(openai_results)
        speech(openai_results)
    except Exception as e:
        speech("Unable to fetch results at the moment")
        print("Unable to fetch results at the moment")
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('hackedurdevice@gmail.com','vxyebfpciieehrkp')
    server.sendmail('hackedurdevice@gmail.com',to,content)
    server.close()
if __name__=="__main__":
    speech("Hello, Iam AI")
    wish_me()
    i=True
    site=["youtube","https://www.youtube.com/"],["google","https://www.google.com/"],["amazon","https://www.amazon.in/"],["flipkart","https://www.flipkart.com/"],["instagram","https://www.instagram.com/"]
    while(True):
        
        speech("How Can I Assist you ?")
        query=take_command().lower()
        if "stop" in query :
            speech("Turning off! AI Assistant designed by Raahul")
            exit()
        for i in site:
            if f"open {i[0]}" in query:
                webbrowser.open(i[1])
        if "wikipedia" in query:
            speech("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=4)
            speech("According to Wikipedia")
            speech(results)
        elif "play music" in query or "play a song" in query: 
            directory_ofsong="C:\\Songs"
            songs=os.listdir(directory_ofsong)
            print(songs)
            v=random.randint(1,2)
            os.startfile(os.path.join(directory_ofsong,songs[v]))
        elif "current time" in query or "time now" in query:
            d=datetime.datetime.now().strftime("%H:%M%S")
            speech(f"The Current Time is {d}")
        elif "open photos" in query:
            path_ofphotos="C:\\Users\\Lenovo\\Pictures\\Saved Pictures"
            os.startfile(path_ofphotos)
        elif "send email" in query:
            try:
                speech("What should I send?")
                content=take_command()
                to="abcd@gmail.com"
                sendEmail(to,content)
                speech("Email has been sent!")
            except Exception as e:
                print(e)
                speech("Problem Encoutered, Unable to Send the Mail")
        elif "using artificial intelligence" in query or "open ai" in query:
            openaifunc(query)
        else:
            if query!='none':
                webbrowser.open(query)
            else:
                exit()
