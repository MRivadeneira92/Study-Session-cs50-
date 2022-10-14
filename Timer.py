import time 
from datetime import datetime
from Functions import timer

# Ask user for the ammount of timers #
print("How many timers?:")
user_ammount = input()
if user_ammount.isnumeric() is False:
    print("Input a valid number")
print("Make timers continuous?[y/n]:")
anwser = input()

# Data to be saved #
user_timer = {}
timers = []

# Ask user for time and save then in a dictionary # 
for i in range(0, int(user_ammount)):   
    print("How many hours?:")
    user_hour = input()
    if user_hour.isnumeric() is False:
        user_hour = 0
    if int(user_hour) > 24:
        user_hour = 24
    user_timer["user_hour"] = int(user_hour)
    print("How many minutes?:")
    user_min = input()
    if user_min.isnumeric() is False:
        user_min = 0
    if int(user_min) > 59:
        user_min = 59
    user_timer["user_min"] = int(user_min)
    print("How many seconds?")
    user_sec = input()
    if user_sec.isnumeric() is False :
        user_sec = 0
    if int(user_sec) > 59:
        user_sec = 59
    user_timer["user_sec"] = int(user_sec)
    timers.append(user_timer)
    if i == int(user_ammount) - 1: 
        break
    else: 
        print("Timer saved!")
        print("Next timer")

# Timer implementation # 
for i in range(0, len(timers)):
    print("Timer number", int(i)+1)
    timer(timers[i]["user_hour"], timers[i]["user_min"], timers[i]["user_sec"] )
    if i == len(timers) - 1:
        break

    while(True):
        if anwser == "y" or anwser == "yes":
            break
        print("Start next timer?: [y/n]")
        x = input()
        if x == "yes" or x == "y":
            break
        else:
            continue

print("DONE!")
