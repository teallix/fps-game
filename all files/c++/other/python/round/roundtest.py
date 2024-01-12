import time
import random

def main():
    ai = input("This is a random printing program that prints two random numbers divided by each other and rounds them to the nearest number. Type 'ok' to start\n")
    
    
    if ai == "ok":
        x = random.randint(1,100)
        y = random.randint(1,100)
        print(x, "/", y, "=", su(x, y))
        time.sleep(1)
        print(round(su(x, y)))
        
    elif ai == "no":
        quit()
        
    else:
        time.sleep(1)
        main()
    
def su(x, y):
    return x / y

main()