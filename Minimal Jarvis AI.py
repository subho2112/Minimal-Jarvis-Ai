import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning !")
        print("Good Morning !\n")
        
    elif hour>=12 and hour<16:
        speak("Good Noon !")
        print("Good Noon !\n")

    elif hour>=16 and hour<18:
        speak("Good Afternoon !")
        print("Good Afternoon !\n")

    else:
        speak("Good Evening !")
        print("Good Evening !\n")
    
    speak("Hello Sir.  I am Jarvis.  Your Vortual Asistance.  Please tell me how may i help you?")
    print("Hello Sir.  \nI am Jarvis.  \nYour Vortual Asistance.  \nPlease tell me how may i help you?\n")
    print("---------------------------:::instruction to use this AI:::--------------------------- \n\t------------Say (you have to from your mouth) something you want to do with your AI-------------\nExample(1):---say open google:----It will automaticly openn google for you.\nExample(2):---Say what is time now:----It will say time now. \nExample(3):---you can say open youtube; open gmail; open instagram; open facebook;\nExample(4):---You can say anyword and then just say WIKIPEDIA, Just like say Salman Khan Wikipedia, it will speak some information about salman khan")
         
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")  

    except Exception as e:
        #print(e)

        print("Say that again please....")  
        return "None"
    return query  
    
if __name__ == "__main__":
    wishme()
    while True:    
        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak("Ok subho. I am searching Wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "who are you" in query:
                print("I am jarvis. Your Virtual Asistance. You creat me. So I am thankful to you. Please tell me how  may I help you");
                speak("I am jarvis. your virtual asistance. You creat me. So I am thankful to you. Please tell me how  may I help you");
                

        elif "jarvis" in query:
                speak("Yes Sir. Please tell me how can i help you ?");
                print("Yes sir. Please tell me how can i help you ?");

        elif 'open youtube' in query:
            speak("ok Subho. i am opening youtube")
            webbrowser.open("youtube.com")
            speak("Here your youtube sir.  Enjoy!")
        
        elif 'open google' in query:
            speak("ok Subho. i am opening gogle")
            webbrowser.open("gogle.com")
            speak("Here your google sir. search whatever you want.")

        elif 'open facebook' in query:
            speak("ok Subho. i am opening your facebook handle")
            webbrowser.open("facebook.com")
            speak("Here your facebook handle. Enjoy with friends ")

        elif 'open whatsapp' in query:
            speak("ok Subho. i am opening your whtsapp handle")
            webbrowser.open("web.whatsapp.com")
            speak("Here your whatsapp sir. Enjoy your chatt!")
        
        elif 'open instagram' in query:
            speak("ok Subho. i am opening your instagram handle")
            webbrowser.open("instagram.com")
            speak("Here your instagram sir")

        elif 'open mail' in query:
            speak("ok Subho. i am opening your gmail")
            webbrowser.open("mail.google.com")    
            speak(" here your gmail sir.")

        elif 'open my google account' in query:
            speak("ok Subho. i am opening your personal gogle acount")
            webbrowser.open("myaccount.google.com")
            speak("Its your gogle acounts sir. Please Be sceure")

        elif 'open get into pc' in query:
            speak("ok Subho. i am opening get into pc")
            webbrowser.open("getintopc.com")
            speak("Here your getintopc sir. Please be carefull when download and using pirated software ")
            
        elif 'github' in query:
            speak("ok subho. I am opening github")
            webbrowser.open("github.com")
            spwak("Here your  github sir")
        
        #elif 'play music' in query:
            #music_dir=
            #songs = os.listdir(music_dir)
            #print(songs)
            #os.startfile(os.path.join.(music_dir, songs[0]))

        elif 'the time'  in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Subho, the time is{strTime}")

        elif 'open control panel' in query:
            cppath = "C:\\Programe Files(86)\\SUBHO\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools"
            speak("ok subho. I am opening Control Panel")
            os.startfile(cppath)

        elif 'bye' in query:
            speak("Good bye subho. Thanks for giving me time. Have agood day")
            exit()
            

       
         
        
        

        



            
