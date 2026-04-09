import time
import sys

while True:
    from datetime import datetime
    now = datetime.now()
    print (f'{now.month}/{now.day}/{now.year}/{now.hour}/{now.minute}/{now.second}', end='\r')
    time.sleep(1)