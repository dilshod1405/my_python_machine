
import time
import datetime


try:
    while True:
        current_time = datetime.datetime.now().strftime("%x")
        print(current_time)
        time.sleep(2)

except KeyboardInterrupt:
    print("stoped")
