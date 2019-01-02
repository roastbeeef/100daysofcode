"""
100 days of code. challenge 1, pomodoro timer.
"""
from datetime import datetime, timedelta, time
import os

def pomodoro(time_target):
    time_target = timedelta(seconds=time_target*60)
    time_alarm = datetime.now() + time_target
    time_sleep = (time_alarm - datetime.now()).seconds
    time.sleep(time_sleep)
    os.system('say "Times up."')

pomodoro(1)

