import time as t

while True:
    ai == input("How long? Choose from: 60s[1], 120s[2], 180s[3], 240s[4], 300s[5]\n")
    
    if ai == "1":
        for x in range(1, 61):
            print(x)
            t.sleep(1)
            
    elif ai == "2":
        for x in range(1, 121):
            print(x)
            t.sleep(1)
            
    elif ai == "3":
        for x in range(1, 181):
            print(x)
            t.sleep(1)
            
    elif ai == "4":
        for x in range(1, 241):
            print(x)
            t.sleep(1)
            
    elif ai == "5":
        for x in range(1, 301):
            print(x)
            t.sleep(1)
            
    elif ai == "no":
        break
    
    elif ai != ("1", "2", "3", "4", "5", "no"):
        t.sleep(0.1)