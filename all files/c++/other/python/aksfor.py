import time as t

while True:
    ai = input("Generate?\n")
    
    if ai == "yes":
        for x in range(1, 61):
            print(x)
            t.sleep(1)
            ask()
            
    elif ai == "no":
        break
    
    elif ai != ("yes", "no"):
        t.sleep(0.1)
        
def ask():
    ais = input("More time?\n")
    
    if ais == "yes":
        def main():
            aif = input("How long? Choose from: 60s[1], 120s[2], 180s[3], 240s[4], 300s[5]\n")
            
            if aif == "1":
                for x in range(1, 61):
                    print(x)
                    t.sleep(1)
                            
            elif aif == "2":
                for x in range(1, 121):
                    print(x)
                    t.sleep(1)
                    
            elif aif == "3":
                for x in range(1, 181):
                    print(x)
                    t.sleep(1)
                            
            elif aif == "4":
                for x in range(1, 241):
                    print(x)
                    t.sleep(1)
                            
            elif aif == "5":
                for x in range(1, 301):
                    print(x)
                    t.sleep(1)
                            
            elif aif == "no":
                quit()
                            
            elif aif != ("1", "2", "3", "4", "5", "no"):
                t.sleep(0.1)
                main()
                             
    elif ais == "no":
        quit()
                
    elif ais != ("yes", "no"):
        t.sleep(0.1)