import datetime
from  speech.speaker import speak

def wishMe():
    hour = datetime.datetime.hour
    
    if hour >= 0 and hour < 12:
        speak('Good Morning Sir.')
    elif  hour >= 12 and hour < 15:
        speak('Good Afternoon Sir.')
    elif hour >=15 and hour < 20:
        speak('Good Evening Sir.')
    else:
        speak('Good Night Sir.')