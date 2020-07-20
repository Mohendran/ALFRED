from  utils import website, cleaner
from speech.speaker import speak

import wikipedia

def find(query):
    query = cleaner.cleanUp(query, ['wikipedia', 'what', 'who', 'is', 'are', 'a', 'at', 'is', 'in', 'on', 'search', 'for', 'from'])
    print('Searching Wikipedia for ' + query)
    result = wikipedia.summary(query, sentences=2)
    print(result)
    speak(result)