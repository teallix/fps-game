import time
import random
import sys

while True:
    def a():
        ai = input("make one?\n")
        
        lisu = [random.randint(1000000,1500000)]
        
        if ai == "yes":
            def ae():
                for i in range(random.choice(lisu)):
                    print(random.randint(10, 99), random.randint(10, 99), random.randint(10, 99), random.randint(10, 99), random.randint(10,99), "|", i)
                    time.sleep(0.00001)
                time.sleep(0.1)

            ae()
            
        elif ai == "no":
            sys.exit()
        
        else:
            time.sleep(0.1)
            
    a()