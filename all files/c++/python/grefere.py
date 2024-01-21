import time

def rt():
    global r
    r = input("yes?\n")
    
    if r == "yes":
        e()
        
    elif r == "no":
        e()
        
def e():
    rh = input("continue?\n")
    
    if rh == "yes":
        f()
        
    elif rh == "no":
        quit()
        
def f():
    time.sleep(1)
    print(r)
    
rt()