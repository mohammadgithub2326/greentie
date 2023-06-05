import pyttsx3
import datetime
import speech_recognition as sr
import os
import webbrowser
import time
#engine to genrate function of modules
engine=pyttsx3.init('sapi5') 
voices=engine.getProperty('voices')
engine.setProperty('voices',(voices[0].id))


#function is created by user,throgh the above engines
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning sir")
    elif hour>=12 and hour<=18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")

    speak("iam   friday ,  iam here to help you ,  ask me something that you want")  
def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("iam listening that you saying sir......")
        r.energy_threshold = 100000
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
       print("let me to recognise.....")
       query = r.recognize_google(audio, language='en-in')
       print(f"user said: {query}\n")

    except Exception as e:
        #pm rint(e)
        return "none"
    query = query.lower()
    return query



        
    #main function ,it should being when the main code is starting 
    
    
    
    
if __name__=="__main__":
    
    wishme()
    while True:
        query = takeCommand()

        if 'hai' in query:
             speak("hello boss")
        elif 'who is your god' in query:
             speak("boss  vaamshi  invented  me  ,  soo  hee  is  my  god") 
        elif 'do you know what i eat today' in query:
             speak("you  didnt said  me  yettt...")
        elif 'is very tasty' in query:
             speak("wow   but  you  didnt  offer  me")   
        elif 'you fool how can you' in query:
             speak("oooppss     sorry  ......")    
        elif 'father' in query:
             speak("sreenu")
        elif 'tell me about seenu' in query:
             speak("he  is  my  gods  father ,  he  scold  my  god  always  but  he   hides   hes  fondness  upon  him") 
        elif 'tell me about your boss' in query:
             speak ("he is vamshi great ,humanity ,handsome ,kindness ,genuise etcetra are the features inbuilt in him i love him finally words come to finish when we start to tell something about him")   
        elif'who is your sir mother' in query:
             speak("lalitha")
        elif'why are you here' in query:
             speak("iam here to help you and to have some fun with me while working with me")
        elif'thanks'in query: 
             speak("oh! its my pleasure ,honor is mine")
        elif 'open youtube' in query:
             webbrowser.open("you tube.com")
        elif 'open instagram' in query:
             webbrowser.open("instagram.com") 
        elif 'open whatsapp' in query:
             webbrowser.open("whatsapp web .com")
        elif 'time' in query:
             strtime = datetime.datetime.now().strftime("%H:%M:%S") 
             speak(f"boss  right   now   the   time   is {strtime}")
        elif 'nahid' in query:
             speak("you must asking about the vegetable king   right............ . . . .,actally  my  boss vamshi use to call him as like..... so i thought ....! ok any way  nahid is a dearest friend of my boss")
        elif 'jyoti' in query:
             speak("ooohhh my god you asking about her           she is a annoying, irritater always ,she is a chubby and fair girl  however she is a my gods bestie she concern him always.... so i respect her obivsely")
        elif'Taj' in query:
             path = "lv_0_20220307221642"
             os.startfile(path)
        elif 'shiva' in query:
             speak("he is the guy who has crush on lakshmi medam ,")
        elif'B T' in query:
             speak("nothing much to say about himm west fellow ,..... hes just a skinny guy but my boss skinny friend ")
        elif'oh shit' in query:
             speak("boss! is any thing wrong")
        elif'you idiot,fool,' in query:
             speak("oh!  is anything wrong with me boss") 
        elif'how long do you work in a day' in query:
             speak("i work 24 by 7 day and night every time boss")   
        elif'how are you' in query:
             speak("great boss ,how do you do")
        elif'you like me ' in query:
             speak("off coourse i love you sir")
        elif'rahul' in query:
             speak("he is fat , beard guy  my boss elder guy basically he loves my boss but he never show  ")
        elif'vidya' in query:
             speak("she is aa aggressive woman... every time never turns to off, either once, but show her kindness in the anger it self  however she is my boss elder siss")
        elif'manoj' in query:
             speak("instead of babu  bangaram  we can use  bava bangaram, actally he is my boss bava")
        elif'vishnu' in query:
             speak("my first liitle hero")
        elif 'varshi' in query:
             speak("and this cute ee  is second one")
        elif'do you like me' in query:
             speak("off course , i love you boss")     
        elif'are you hearing me' in query or 'could you hear me' in query:
             speak("yes  boss  , iam getting your words")
        elif'getting tough' in query:
             speak("no boss  i can hear you excatly")
        elif 'what can you do' in query or 'how will you work' in query:
             speak("i can make several tasks, like , i can operate the web broweser through your command , im very innovative , i learn many things daily to give better service to you i can operate all the system targets through your one command ...,boss ")
        elif'bloody idiot' in query or 'useless'  in query:
             speak("boss  you  dont  pass  your  limits  ,  please dont make me agresive  either  i wont work for you")
        elif"don't mind" in query:
             speak("its  ok  boss never  do  this  again")
        elif'i like' in query:
             speak("boss......how could i know that what you like you never said me.....")
        elif'how attitude' in query:
             speak("yeah ,  because  im  invented  by vamshi")     