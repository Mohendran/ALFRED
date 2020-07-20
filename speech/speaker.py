import pyttsx3
from playsound import playsound

# Initilaizing the Speech Engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def success():
    playsound('speech/assets/success.mp3')

def error():
    playsound('speech/assets/error.mp3')