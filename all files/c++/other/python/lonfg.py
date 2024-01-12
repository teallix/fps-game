import time
import random

def obj():
    ai = input("Type '?'\n")
    
    if ai == "?":
        try:
            while True:
                nu = random.randint(1,100)
                ni = random.randint(1,100)
                x = random.randint(1,100)
                y = random.randint(1,100)
                time.sleep(1)
                pow(x, y)
                zip(nu, ni)
                
        finally:
            mi()
            
    elif ai == "no":
        quit()
        
    else:
        time.sleep(1)
        obj()
            
def mi():
    ob = random.choice(list)
    ais = input("Type 'yes'\n")
    
    if ais == "yes":
        del(ob)
        slice(mi())
        slice(obj())
    
    elif ais == "no":
        quit()
        
    else:
        print(ob)
        time.sleep(1)
        mi()
        
obj()