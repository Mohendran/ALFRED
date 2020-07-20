from  utils import website, cleaner
from speech.speaker import success

def filter(query):
    query = cleaner.cleanUp(query, ['youtube', 'play', 'open', 'what', 'who', 'is', 'are', 'a', 'at', 'is', 'in', 'on', 'search', 'for', 'from'])
    print('Searching Youtube for ' + query)
    website.open('https://www.youtube.com/results?search_query=' + query)
    success()