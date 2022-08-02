import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pandas as pd

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 165)
voices = engine.getProperty('voices')
df = pd.read_csv('database.csv')
#engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
##        with sr.Microphone() as source:
##            print('listening...')
##            voice = listener.listen(source)
##            command = listener.recognize_google(voice)
##            command = command.lower()
##            if 'bank' in command:
##                command = command.replace('bank', '')
##                print(command)
        print("Bot:What can i do for you?")
        command = input("You:")
    except:
        command='error'
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'balance' in command:
        talk('Please!, Enter you account number: ')
        acc_entered = int(input('Please!, Enter you account number: '))
        for i in range(0,len(df)):
            if acc_entered == df.account[i]:
      
                talk(f'Welcome {df.name[i]}!')
                print(f'Welcome {df.name[i]}!')
                
                talk(f'Your current account balance is {df.balance[i]} rupees')
                print(f'Your current account balance is {df.balance[i]} rupees')
                break
            if i == len(df)-1:
                print('Please check your Account number!')
                talk('Please check your account number')
    elif 'transaction' in command:
        acc_entered = int(input('Please!, enter you account number: '))
        talk('Please!, enter your account number: ')
        for i in range(0,len(df)):
            if acc_entered == df.account[i]:
                print(f'Welcome {df.name[i]}!')
                talk(f'Welcome {df.name[i]}!')
                print('---------------Recent transaction---------------------')
                print('---------details--------debit-----credit----------bal-')
                print('     Home loan          12500                  1400000')
                print('     Cheque no.420               100000        1500000')
                talk('Your recent transaction are as follows')
                break
                #talk(f'Your current account balance is {df.balance[i]} rupees')
            if i == len(df)-1:
                print('Please, Check entered account number')
                talk('Pleasec Check enetered account number')
    elif 'cheque' in command:
        req = int(input('Please!, enter your account number: '))
        talk('Please!, enter your account number: ')
        for i in range(0,len(df)):
            if req == df.account[i]:
                print(f'Welcome {df.name[i]}!')
                talk(f'Welcome {df.name[i]}!')
                talk("Please Enter Your complete address: ")
                print("Please Enter Your complete address: ")
                talk('Your Request for cheque book has been successfully accepted!')
                print('Request accepted!')
                break
                #talk(f'Your current account balance is {df.balance[i]} rupees')
            if i == len(df)-1:
                print('Please, Check entered account number')
                talk('Pleasec Check enetered account number')
    else:
        talk('Please repeat the command')


while True:
 run_alexa()
 

