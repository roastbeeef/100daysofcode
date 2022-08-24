from datetime import date
from datetime import datetime
from datetime import timedelta
import time
import os

# looping isnt working properly but it doesnt really matter, the idea here was to practice using timedeltas

def pomodoro(
    work_time_mins: int,
    break_time_mins: int,
    repeat: int):

    convert_mins_to_seconds = lambda x: timedelta(seconds=(x*60))
    
    timer_length = convert_mins_to_seconds(work_time_mins)
    break_time = convert_mins_to_seconds(break_time_mins)

    while repeat:
        b_time = break_time
        w_time = timer_length
        while timer_length:
            w_time -= timedelta(seconds=1)
            time.sleep(1)
            print(f'say {w_time} of work remaining', end='\r')
        if repeat:
            print(f'congratulations, time for a {b_time} minute break')
            while b_time:
                b_time -= timedelta(seconds=1)
                time.sleep(1)
                print(f'{b_time} of break time remaining', end='\r')
        else:
            print(f'times up, well done on being productive!')
        repeat -= 1


pomodoro(0.1, 0.1, 2)