# To enter weird terminal, run this code and type 'fc' into the blank terminal
# You can't do anything there but type, but it is a cool glitched place
import time
import random

lists = ['.', '..', '...', '....', '.....', '......', '.......', '........', '.........', '..........']
def main():
    num1 = float(1)
    num2 = float(2)
    
    print(num1 * num2)
    jk()
    
def loo():
    for x in range(1, 6):
        print(x)
        time.sleep(0.2)
    
    
def jk():
    time.sleep(0.5)
    print(float(1))
    time.sleep(0.1)
    print(float(2))
    time.sleep(0.1)
    print(float(3))
    time.sleep(0.5)
    loop()
    
def loop():
    print(1 / 3)
    time.sleep(0.5)
    print(2 + 98)
    time.sleep(0.5)
    print(141 * 141)
    lool()
    
def lool():
    try:
        nuum1 = float(24)
        nuum2 = float(141)
        
        print(nuum1)
        time.sleep(0.5)
        print(nuum2)
        time.sleep(0.5)
        print(nuum1 + nuum2)
        time.sleep(0.5)
    finally:
        loor()
        
def loor():
    try:
        print(random.choice(lists))
        time.sleep(0.5)
    finally:
        loo()
    
main()