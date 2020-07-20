from  speech.speaker import success
from utils import cleaner

def filter(query):
    query = cleaner.cleanUp(query, ['search', 'for', 'npm', 'in', 'packages', 'package', 'module'])
    print('Searching NPM for ' + query)
    success()