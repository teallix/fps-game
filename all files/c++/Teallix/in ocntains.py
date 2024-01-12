import time
import random

def start():
    ai = input("Type anything\n")
    
    if ai in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '/', ';', '<', '>', '?', ':', '[', ']', '{', '}', '|', '-', '=', '_', '+', '!', '@', '#', '%', '"', '^', '&', '*', '(', ')']:
        print("1")
        time.sleep(1)
        def end():
            i = ['a']
            
            for i in range(random.randint(100,1000)):
                print(i)
                time.sleep(0.01)
            
        end()
        
    else:
        time.sleep(1)
        start()
        
start()