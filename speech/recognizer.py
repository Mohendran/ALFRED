import speech_recognition as sr
from speech.speaker import error

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        #speak('Sorry sir! I didn\'t get that! Try typing the command!')
        error()
        print('Sir. Im listening in the background. Was that a command ?')
        #query = str(input('Command: '))
        query = ''

    return query