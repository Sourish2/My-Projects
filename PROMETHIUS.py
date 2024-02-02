import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from email.message import EmailMessage
import ssl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import fandom
import pywhatkit
import pyjokes

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')

    speak('I am Promethius, Your wish is my command')
    print('WELCOME TO PROMETHIUS, YOUR AVERAGE VIRTUAL ASSISTANT')

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print('Recognising..')
        query= r.recognize_google(audio, language='en-in')
        print("User said: ", query)


    except Exception as e:
        print('Say that again please...')
        speak('sorry, I did not quite get that')
        return 'None'
    return query

def sendEmail(reciever_email):
    email_sender = 'sourishdatta8@gmail.com'
    email_password = 'yeinushxavvxwtne'
    email_reciever = reciever_email

    subject = input('Enter Subject: ')
    body = input('Enter Content: ')

    en = MIMEMultipart()
    en['From'] = email_sender
    en['To'] = email_reciever
    en['Subject'] = subject
    en.attach(MIMEText(f'''<html>
                           <body>
                                <h1 style="text-align:center;color: #565051;">MESSAGE FROM PROMETHIUS</h1>
                                <p style="color:#00FFFF;">{body}</p>
                           </body>
                        </html>''','html','utf-8'))
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, en.as_string())
        print('email sent')


if __name__=='__main__':
    wishMe()
while True:
    query=takeCommand().lower()

    if 'wikipedia' in query:
        speak('Searching Wikipedia...Please Wait')
        query.replace('wikipedia',"")
        results = wikipedia.summary(query,sentences=2)
        speak('According to Wikipedia')
        speak(results)
    elif 'open youtube' in query:
        search=input('Enter Search Target: ').replace(' ','+')
        webbrowser.open(f'https://www.youtube.com/results?search_query={search}')
    elif 'open google' in query:
        search=input('Enter Search Target: ')
        speak('Okay, this is what I found')
        pywhatkit.search(search)
    elif 'special search' in query:
        Universe=input('Enter the franchise or universe your search belongs to, example harry potter, marvel etc: ')
        Universe.lower()
        Universe.replace(' ','')
        fandom.set_wiki(Universe)
        try:
            search=input('Enter Search Target: ')
            page=fandom.page(search)
            path=page.url
            webbrowser.open(path)
            speak(fandom.summary(search, Universe))
        except Exception as e:
            print("Error 404, Please Try again")
            speak("Error 4-0-4, Please Try again")
    elif 'the time' in query:
        strTime=datetime.datetime.now().strftime('%H:%M:%S')
        speak('Sir, the time is '+ strTime)
    elif 'open steam' in query:
        path="C:\\Program Files (x86)\\Steam\\steam.exe"
        os.startfile(path)
    elif 'email' in query:
        recieverid=input('Enter reciever\'s email id: ')
        sendEmail(recieverid)
        speak('email sent')
    elif 'play music' in query:
        speak('youtube music or spotify?')
        choice=input('Youtube Music or Spotify? ')
        choice.lower()
        if choice == 'spotify':
            path="C:\\Users\\souri\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(path)
            time.sleep(20)
        elif choice== 'youtube music':
            webbrowser.open('music.youtube.com')
            time.sleep(20)
    elif 'goodbye' in query:
        print('Goodbye User, I hope to see you soon')
        speak('Goodbye User, Please visit again')
        exit()
    elif 'joke' in query:
        myjoke = pyjokes.get_joke('en',category='neutral')
        print(myjoke)
        speak(myjoke)
    elif 'thank' in query:
        print('you are quite welcome')



