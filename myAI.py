import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import speech_recognition as sr

# calling microsoft API which speek out.
engin = pyttsx3.init('sapi5')
voices = engin.getProperty('voices')

engin.setProperty('voice', voices[1].id)

# this fn speek out
def speak(audio):
    engin.say(audio)
    engin.runAndWait()

# say time and thankfull massages
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning ! Arefin")

    elif hour>=12 and hour<18:
        speak("Good Afternoon ! Arefin")

    else:
        speak(" Good Evening ! ")

    speak("I am Your AI Sir. Please tell me how my i help you")

def takeCommand():
    # it takes microphone input from the user and returns string output

    # r = sr.Recognizer() #helping for recognize input
    # m = sr.Microphone()
    # with m as source:
    #     print("Listening... ")
    #     r.pause_threshold = 1
    #     audio = r.listen(source)

    try:
        print("Recognizing...")    
        # query = r.recognize_google_cloud(audio, language='en-in') #Using google for voice recognition.
        query = input("Give Instruction : ")
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:   
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
    
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('badboysaim46@gmail.com', 'pass')
    server.sendmail('arefinreza46@gmail.com', to, content)
    server.close()
# this is main fn
if __name__ == "__main__":
    
    wishMe()
    while True:
        queary = takeCommand().lower()

        # logic for executing tasks based o query 
        if 'wikipedia' in queary:
            speak('Searching Wikipedia....')
            queary = queary.replace("wikipedia", "")
            results = wikipedia.summary(queary, sentences = 2)
            speak("According to Wikipedia ")
            print(results)
            speak(results)
            
        elif 'youtube' in queary:
            webbrowser.open("youtube.com")
        elif 'google' in queary:
            webbrowser.open("google.com")
        elif 'facebook' in queary:
            webbrowser.open("facebook.com")
        elif 'stackoverflow' in queary:
            webbrowser.open("stackoverflow.com")

        elif 'w3school' in queary:
            webbrowser.open("www.w3schools.com")
        elif 'my pictures' in queary:
            picture_dir = 'D:\\picture\\Camera2'
            pic = os.listdir(picture_dir)
            print(pic)
            os.startfile(os.path.join(picture_dir, pic[0]))
        elif 'the time' in queary:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
        elif 'open code' in queary:
            codePath = "C:\\Users\\arefi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to arefin' in queary:
            try:
                speak("What should I Say? ")
                content = takeCommand()
                to = "arefinsaim46@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("Sorry Sir.. I am not able to send this email ")