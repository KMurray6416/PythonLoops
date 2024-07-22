
import random

week_day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
time_of_day = ['morning', 'afternoon', 'evening']
mood = ['chipper', 'aggravated', 'devious', 'exhausted', 'energetic', 'content']

for i in range(len(week_day)):
    for x in range(3):
        num = random.randint(0,5)
        print("on", week_day[i], time_of_day[x], "you were", mood[num])