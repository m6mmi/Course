from datetime import datetime

# Morning, Day, Evening or Night.
#  = datetime.now().hour


def what_time(hour):
    if hour < 5:
        return "Night"
    elif hour < 10:
        return "Morning"
    elif hour < 18:
        return "Day"
    elif hour < 22:
        return "Evening"
    elif hour < 24:
        return "Night"
