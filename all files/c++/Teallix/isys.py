import time
import random
import sys

def start():
    ai = input("Start?\n")
    
    if ai in ['/', 'yes']:
        for i in range(random.randint(100000,150000)):
            print(random.randint(10,99), random.randint(10,99), random.randint(10,99), "|", i)
            time.sleep(0.0001)
        time.sleep(1)
        start()
        
    elif ai == "no":
        sys.exit()
        
    else:
        time.sleep(1)
        start()
        
start()