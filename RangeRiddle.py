
import random

mood = ['Happy','Sad','Energetic', 'Calm']
week_day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


for i in range(len(week_day)):
        num = random.randint(0,3)
        print("on", week_day[i], "you were feeling", mood[num])
 
