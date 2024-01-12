import time
# import random
# unless used will show error

def gameStart():
    enter = input("Enter your name to play game\n")
    time.sleep(0.75)
    print("Hello, " +enter+ ", this is a game designed to make you cry of confusion")
    time.sleep(2.5)
    print("Sunday, February 11th, 1996, 0400")
    time.sleep(2)
    print("17°51'50\"N 77°17'53\"W\", off the coast of Jamaica") # (fixed)reminder to change the '' to "" before realease
    time.sleep(2)
    print("The weather is a cool, windy wet that kind of reminds your of your home back in Shreveport")
    time.sleep(2)
    print("You're on your boat, the \"Enforcer\", as you named it")
    time.sleep(2)
    print("You swear that 1 day you'll get a new one, since it's a rough 14 year old boat")
    time.sleep(2)
    print("\"Do i go to land, or stay here\", you ask yourself")
    time.sleep(2)
    print("\"Should I though?\"")
    time.sleep(1.5)
    print("Do you go to land(1), or not(2)?") # change the (1) and (2) before release
    time.sleep(1)
    goOrNotLandWater()
    
def goOrNotLandWater():
    enter1 = input("")
    
    if enter1 == "1":
        wentToLand()
    
    elif enter1 == "2":
        wentToWater()
    
    elif enter1 == "back":
        time.sleep(0.5)
        gameStart()
    
    elif enter1 == "no":
        quit()
        
    else:
        time.sleep(0.5)
        print("Wait, what did you say?")
        time.sleep(0.5)
        goOrNotLandWater()

def wentToLand(): # finish
    return

def wentToWater(): # finish
    return

gameStart()