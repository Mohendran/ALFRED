import datetime
from enums.DaySession import DaySession

def get_session_name():
    hour = datetime.datetime.hour
    
    if hour >= 0 and hour < 12:
        return DaySession.MORNING
    elif  hour >= 12 and hour < 15:
        return DaySession.AFTERNOON
    elif hour >=15 and hour < 20:
        return DaySession.EVENING
    else:
        return DaySession.NIGHT
