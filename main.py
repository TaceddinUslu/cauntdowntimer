import time


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeFormat = "{:02d}:{:02d}".format(mins, secs)
        print(timeFormat)
        time.sleep(1)
        time_sec -= 1
    print("00:00")

time_sec = input("enter your seconts: ")

countdown(int(time_sec))