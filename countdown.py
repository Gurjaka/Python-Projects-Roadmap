import time
import playsound

wait = input('Time in seconds: ')
while True:
    try:
        wait = int(wait)
        break
    except ValueError:
        print('Invalid input! Must be integer!')

for i in range(wait, 0, -1):
    print(i)
    time.sleep(1)

playsound.playsound("./alarm.mp3")
