from playsound import playsound
import time

CLEAR  = "\033[2J"
CLEAR_AND_REURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left  = seconds - time_elapsed
        minutes_left = time_left // 60 #125 //60 = 2
        seconds_left = time_left % 60 #125 % 60 = 5

        print (f"{CLEAR_AND_REURN}Alarm will Sound in: {minutes_left:02d}:{seconds_left:02d}") #2 digits adding with Zero
    
    playsound("alarm.mp3")

minutes = int(input("How many Minutes to wait :"))
seconds = int(input("How many Seconds Nee to wait :"))
total_seconds = minutes * 60 + seconds

alarm(total_seconds)
