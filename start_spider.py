import os
import time

while True:
    try:
        os.system('python3 main.py')
    except Exception as e:
        print(e)
    time.sleep(7200)
