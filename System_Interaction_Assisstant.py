import os
import pyttsx3
import datetime
import speech_recognition as sr

pyttsx3.speak("My name is DOBBY")
print("DOBBY")
pyttsx3.speak("I'M VIRTUAL ASSISTANT HOW MAY I HELP YOU !!")
print("I'M VIRTUAL ASSISTANT HOW MAY I HELP YOU !!")

while True:
    pyttsx3.speak('please tell me how can i help u')
    print('How can dobby help you :', end='')
    r = sr.Recognizer()
    with sr.Microphone() as Source:
        print("Start ..")
        audio = r.listen(Source)
        print("Stop ..")
    a = r.recognize_google(audio)
    if "list" in a :
        print("I can start app like: ")
    else:
        if('run' in a or 'open' in a) and ('chrome' in a or 'browser' in a or 'google' in a):
            pyttsx3.speak('opening chrome browser for you')
            os.system('chrome')
        elif('who are you' in a or 'what is your name ' in a or 'tell me about yourself' in a or 'tell me about you ' in a or 'introduce yourself' in a):
            pyttsx3.speak('my name is DOBBY and I am your virtual assistant also i am here to help you in doing any task which are present in my list. Type list to find list of all tasks')
        elif('run' in a or 'open' in a) and ('notepad' in a or 'text editor' in a):
            pyttsx3.speak('opening notepad for you')
            os.system('notepad')
        elif('run' in a or 'open' in a) and ('microsoft edge' in a or 'microsoft browser' in a):
            pyttsx3.speak('opening microsoft edge for you')
            os.system('msedge')
        elif('run' in a or 'open' in a) and ('whatsapp' in a or 'whats app' in a):
            pyttsx3.speak('opening whatsapp  for you')
            os.system('chrome whatsapp.com')
        elif('run' in a or 'open' in a) and ('telegram' in a):
            pyttsx3.speak('opening telegram  for you')
            os.system('chrome telegram.com')
        elif('run' in a or 'open' in a) and ('instragram' in a or 'instra' in a):
            pyttsx3.speak('opening instragram  for you')
            os.system('chrome instragram.com')
        elif('run' in a or 'open' in a) and ('calculator' in a or 'calc' in a):
            pyttsx3.speak('opening calculator for you')
            os.system('calc')
        elif('run' in a or 'open' in a) and ('zoom' in a):
            pyttsx3.speak('opening zoom  for you')
            os.system('chrome zoom.us')
        elif('run' in a or 'open' in a) and ('windows media player' in a):
            pyttsx3.speak('opening windows media player for you')
            os.system('wmplayer')
        elif('run' in a or 'open' in a) and ('vlc media player' in a or 'media player' in a or 'vlc' in a):
            pyttsx3.speak('opening vlc media player for you')
            os.system('vlc')
        elif('run' in a or 'open' in a) and ('control panel' in a):
            pyttsx3.speak('opening control panel for you')
            os.system('control panel')
        elif('run' in a or 'open' in a) and ('facebook' in a or 'fb' in a):
            pyttsx3.speak('opening facebook  for you')
            os.system('chrome facebook.com')
        elif('run' in a or 'open' in a) and ('youtube' in a or 'youtube.com' in a):
            pyttsx3.speak('opening youtube for you')
            os.system('chrome youtube.com')
        elif('date' in a or 'dinak' in a):
            today = datetime.date.today()
            pyttsx3.speak(today)
            print(today)
        elif('open'in a or 'run'in a) and ('google maps'in a or 'maps'in a):
            pyttsx3.speak('opening google maps')
            os.system('chrome https://www.google.com/maps/')
        elif('open'in a or 'run'in a or 'today'in a) and ('today weather'in a or ' weather'in a or 'weather report'in a):
            pyttsx3.speak('opening weather report')
            os.system('chrome https://www.google.com/search?q=weather&rlz=1C1CHBF_enIN919IN919&oq=weather&aqs=chrome..69i57j35i39j0i20i131i263i395i433j0i395l3j69i60l2.1975j1j7&sourceid=chrome&ie=UTF-8')
        elif('open'in a or 'run'in a ) and ('amazon.com' in a or 'amazon.in'in a or 'shoping web site' in a or 'shoping site'in a):
            pyttsx3.speak('opening amazon')
            os.system('chrome https://www.amazon.in/ ')
        elif('open'in a or 'run'in a or 'play'in a) and ('music'in a or 'play music'in a or 'song'in a):
            pyttsx3.speak('playing music for you')
            os.system('chrome https://www.youtube.com/')
        elif('hi'in a or 'hello'in a):
            pyttsx3.speak('hello sir wellcome you please assign a task')
            print('hello sir wellcome you please assign a task')
        elif(('do not'in a) or ('not' in a) or ('does not' in a) or ('not open' in a)):
            pyttsx3.speak("Sorry Sir, I can't do for you. Tell Veer Bhadra to Update me.")
        elif('exit' in a or 'close' in a):
            pyttsx3.speak('closing program')
            break
        else:
            pyttsx3.speak('sorry sir i am not able to understand what do you want.  type EXIT or close to leave the program !')
