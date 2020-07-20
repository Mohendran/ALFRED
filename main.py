# imports
from speech import recognizer
from commands import googler, wiki, youtuber, npm
import sys
    
if __name__ == '__main__':

    while True:
    
        query = recognizer.listen()
        if (query):
            query = query.lower()
            
            if 'google' in query:
                googler.filter(query)
                
            elif 'npm' in query:
                npm.filter(query)
            
            elif 'play' in query or 'youtube' in query:
                youtuber.filter(query)
                
            elif 'wikipedia' in query:
                wiki.find(query)
                
            elif 'search' in query or 'show' in query or 'what' in query or 'who' in query or 'which' in query or 'when' in query or 'how' in query:
                googler.find(query)
                
            elif 'bye' in query or 'thanks' in query or 'thank you' in query or 'okay' in query or 'ok' in query:
                print('Bye. Take Care!')
                sys.exit()
            else:
                continue
