from datetime import datetime

current_hour = datetime.now().hour

if 6 < current_hour < 12:
    print("Good morning!")
elif 12 <= current_hour < 17:
    print("Good day!")
elif 17 <= current_hour < 21:
    print("Good eavning")
else:
    print("Good night")
