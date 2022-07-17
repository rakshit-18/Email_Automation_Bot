import email
from email import message
from http import server
import smtplib

from unicodedata import name
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

priority_email_list = {
    'recruiter' : 'recruiter@google.com',               #You can add more people in your priority list
    'homie'     : 'homie123@gotmail.com',
    'dad'       : 'dad007@gmail.com',
    'mom'       : 'mom001@gmail.com',
    'bro'       : 'bro9908@gmail.com'
}

def bot_talk(text):
    engine.say(text)
    engine.runAndWait()

def bot_getData():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            info=listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_Email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('User_Email', 'User_password')   #Enter your email id and passsword here
    email = EmailMessage()
    email['From'] = 'User_Email'                      #Enter your email id here
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

def get_email_info():
    bot_talk('Whom would you like to send an email')
    name = bot_getData()
    receiver = priority_email_list[name]
    print(receiver)

    bot_talk('What is the subject of your mail ?')
    subject = bot_getData()

    bot_talk('Please tell the text for your mail')
    message = bot_getData()

    send_Email(receiver, subject, message)
    bot_talk('Your mail is sent')
    bot_talk('Do you want to send another mail ?')
    sendMore = bot_getData()
    if 'yes' in sendMore:
        get_email_info()


get_email_info()
