from PyDictionary import PyDictionary
import pyttsx3
import datetime

engine=pyttsx3.init('sapi5')
rate=engine.getProperty('rate')
engine.setProperty('rate',160)

def speak(audio):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        t1 = "good morning mister", name
        speak(t1)
    elif hour > 12 and hour < 18:
        t2 = "good afternoon mister", name
        speak(t2)
    else:
        t3 = "good evening mister", name
        speak(t3)

def missme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12                                                                                                         :
        s1="good morning miss",name
        speak("s1")
    elif hour>12 and hour<18:
       s2="good afternoon miss",name
       speak(s2)
    else:
       s3= "good evening miss",name
       speak(s3)


if __name__ == "__main__":
  speak("welcome to python dictionary , i'm david i will asist you in this application")
  upp="welcome to python dictionary".upper()
  print(upp)
  speak("so before you get enter in this application,i want to know your details,because every data from our customer are valueable for our organisation")
  speak("so are you agree with me if yes then type yes else type no")
  upp1="If you are get enter into this dictionry press 'yes' else you can press 'no' for come back into this application ".upper()
  print(upp1)
  x=input()
  y="yes"
  z="no"
if (x==y):
    speak("so you are ready to get your data")
    speak("so first of all you give your first name and then last name ")
    speak("then give your date of birth")
    speak("and finally give your gender ")
    print("FIRST NAME: ")
    name=input()
    print("LAST NAME: ")
    name2 = input()
    print("D.O.B(only year):")
    dob=input()
    age=2019-int(dob)
    print("AGE: ",age)
    print("GENDER: ")
    gender=input()
    if (gender=="male"):
        wishme()
        print("Hello Mr",name,"sir")
        speak("once again welcome sir")
        print("DICTIONARY HUB")
        speak("sir please type which word you found")
        dictionary=PyDictionary()
        word=input()
        b=dictionary.translate(word,'hi')
        print(b)
        speak("thank you for visiting our application,have a nice day sir")
        exit()
    elif (gender=="female"):
        missme()
        print("Hello Mrs", name, "madam")
        speak("once again welcome mam")
        print("DICTIONARY HUB")
        speak("madam please type which word you found")
        word = input()
        dictionary=PyDictionary()
        c=dictionary.translate(word,'hi')
        print(c)
        speak("thank you for visiting our application,have a nice day madam")
        exit()
    else:
        speak("sorry sir or madam you are giving some wrong information,so please try next time")
        exit()

elif (x==z):
    speak("have a nice day sir or mam")
    print("Have a nice day sir or mam")
    exit()
else:
    speak("sorry sir/madam,you are not enter valid answer ")
    speak("so you have to leave this application and again start")
    speak("bye bye")
    exit()

