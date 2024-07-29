import time
import winsound  # Note: This module is specific to Windows.

def set_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            winsound.Beep(1000, 1000)  # Frequency: 1000 Hz, Duration: 1000 ms
            break
        time.sleep(1)

alarm_time = input("Set the alarm time (HH:MM:SS): ")
set_alarm(alarm_time)
