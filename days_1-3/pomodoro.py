"""
100 days of code. challenge 1, pomodoro timer.

This is my first commit and it's certainly taken me more than an
hour so far, I've still got two days to finish it so I can spend
a bit of time working on a UI :)

- Need to fix the buffering on carriage return - looks messy.

Here's the challenge from PyBites;
- At its simplest, create a timer for a set duration (eg 20 minutes) 
that "alarms" or notifies you at completion.
- Go a step further and allow the user to specify the amount of time 
the Pomodoro Timer goes for.
- Again, further develop the app by allowing it to loop. That is, 
Pomodoro Time > break time > Pomodoro Time > break time. Just like 
the pros!
- Create a user interface if you have the time! PyGame or argparse 
perhaps? Maybe even make it web based with Flask or your other f
favourite web framework.
"""
from datetime import datetime, timedelta
import time as t
import os

def pomodoro(time_target, time_break, loops):
    time_target = timedelta(seconds=time_target*60)
    break_target = timedelta(seconds=time_break*60).seconds
    time_alarm = datetime.now() + time_target
    time_sleep = (time_alarm - datetime.now()).seconds
    # the main timer starts here.   
    while loops:
        # audible and visual notification
        os.system('cls||clear')
        message = '"Timer Starting"'
        print(message.replace('"',''), end='\r')
        sys.stdout.flush() # stops buffering after CR
        os.system('say {}'.format(message))
        rtime = time_sleep
        # loop to control the visual countdown
        while rtime:
            minutes, seconds = divmod(rtime, 60)
            time_format = 'Time Remaining: {:02d}:{:02d}'.format(minutes, seconds)
            print(time_format, end='\r')
            t.sleep(1)
            rtime -= 1
        # catch 
        if loops > 1:
            message = '"Times up, take a short break."'
            print(message.replace('"',''))
            os.system('say {}'.format(message))
            stime = break_target
            while stime:
                minutes, seconds = divmod(stime, 60)
                time_format = 'Break Remaining: {:02d}:{:02d}'.format(minutes, seconds)
                print(time_format, end='\r')
                t.sleep(1)
                stime -= 1
        else:
            os.system('cls||clear')
            message = '"Times up, well done."'
            print(message.replace('"',''), end='\r')
            os.system('say {}'.format(message))
        loops -= 1

