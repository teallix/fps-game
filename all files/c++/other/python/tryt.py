import time
import random

lists = ["True", "False"]

def min():
    ai = input("Type '?'\n")
    
    if ai == "?":
        try:
            ais = input("Hello there, ?\n")
            
            if ais == "?":
                nu = random.randint(1,100)
                    
                print(nu)
                time.sleep(1)
                main()
                    
        finally:
            print("min is unreachable")
            time.sleep(1)
            main()
            
    elif ai == "no":
        quit()
        
    else:
        time.sleep(1)
        min()
                    
def main():
    nui = "any"
    nuu = random.choice(lists)
    
    if nuu is "True":
        quit()
        
    elif nuu is "False":
        min()
        
    elif nui == "any":
        nui = not callable
        
        if nui is not callable:
            quit()
        
min()