#!/usr/bin/python
import time

def procedure():
   time.sleep(1)
   
while True:
    # measure process time
    t0 = time.ctime()
    procedure()
    print(time.ctime(), "seconds process time")
    
    # # measure wall time
    t0 = time.time()
    procedure()
    print(time.time() - t0, "seconds wall time")
    
# This will print the local time and the seconds will update every 1 second
# Can be changed with the time.sleep() function in the procedure definiton