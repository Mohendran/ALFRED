from googlesearch import search
from speech.speaker import error
from utils import cleaner, website

def find(query):
    websites = []

    query = cleaner.cleanUp(query, ['search', 'for', 'google', 'show'])
    print('Googling for ' + query)
    try:
        for url in search(query,        # The query you want to run
                tld = 'com',  # The top level domain
                lang = 'en',  # The language
                num = 2,     # Number of results per page
                start = 0,    # First result to retrieve
                stop = 2,  # Last result to retrieve
                pause = 2.0,  # Lapse between HTTP requests
                   ):
            if 'https://en.wikipedia.org' not in url:
                websites.append(url)
                print(url)
        website.open(websites[0])
        success()
        
    except:
        error()

def filter(query):
    query = cleaner.cleanUp(query, ['search', 'google', 'for'])
    print('Searching for ' + query)
    website.open('https://www.google.com/search?q=' + query)