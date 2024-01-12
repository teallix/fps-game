import time
import random

while True:
    lists = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '$', '%', '^', '&', '*', ';', ':', '>', '<', '/', '?', '-', '_', '.', ',', '|', '`', '~', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    var1 = random.randint(0,9)
    var2 = random.randint(0,9)
    var3 = random.randint(0,9)
    var4 = random.randint(0,9)
    var5 = random.randint(0,9)
    var6 = random.randint(0,9)
    var7 = random.randint(0,9)
    var8 = random.randint(0,9)
    var9 = random.randint(0,9)
    var10 = random.randint(0,9)
    
    hack = 'auto aim'
    
    ai = input("Generate?\n")
    
    if ai == "yes":
        print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
        
    elif ai == "no":
        break
    
    elif ai == "yess":
        while True:
            print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
            time.sleep(1)
            
    elif ai == "1":
        print(random.choice(lists))
        
    elif ai == "/hack_auto_aim":
        def edx():
            print(var1, var2, var3, var4, var5, var6, var7, var8, var9, var10)
            time.sleep(2)
            print("Unable to load hack:", hack)
            time.sleep(1.5)
            print(hack, "Unavailable at this time")
            time.sleep(1)
            print("Error loading", hack, ", Does user wish to exit?")
            
            ai = input()
            
            if ai == "yes":
                exit()
                
            elif ai == "no":
                return input
            
            else:
                return input
            
        edx()
    elif ai == "/py_exit":
        break
        
    else:
        time.sleep(1)