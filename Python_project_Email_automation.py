import smtplib
import speech_recognition as sr
from email.message import EmailMessage
import pyttsx3

listener = sr.Recognizer()

tts = pyttsx3.Engine()

def talk(text):
    tts.say(text)
    tts.runAndWait()

def sound():
    with sr.Microphone() as source:
        print("Listening......")
        listener.adjust_for_ambient_noise(source)
        
        while True:
            try:
                voice = listener.listen(source, timeout=5)
                data = listener.recognize_google(voice)
                print(data)
                
                if data:
                    return data.lower()
                else:
                    print("Sorry, I did not hear. Please try again.")
                    talk("Sorry, I did not hear. Please try again.")
                    
            except sr.UnknownValueError:
                print("Sorry, I did not hear. Please try again.")
                talk("Sorry, I did not hear. Please try again.")

emails = {"first": "utkarshakale06@gmail.com"}

def mail_send(receiver, subject, body):
    server = smtplib.SMTP("smtp.gmail.com", "587")
    server.starttls()
    server.login("cseiiia35@rgcer.edu.in", "umzgwwaxxtdjyziy")
    
    mail = EmailMessage()
    mail["From"] = "cseiiia35@rgcer.edu.in"
    mail["To"] = receiver
    mail["Subject"] = subject
    mail.set_content(body)
    server.send_message(mail)

def final():
    talk("Whom do you want to send the Email?")
    name = sound()
    receiver = emails.get(name)
    
    if receiver:
        talk("What is the subject of the Email?")
        subject = sound()
        talk("What is the body of your Email?")
        body = sound()
        mail_send(receiver, subject, body)
        print("Email has been successfully sent.")
        talk("Email has been successfully sent.")
    else:
        print("Recipient not found in the email dictionary.")

final()