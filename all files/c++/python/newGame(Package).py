import time
# import random
# unless used will show error
gender = 'male', 'female'
race = 'white', 'black', 'asain', 'hispanic', 'middle eastern'
country_of_origin = 'america', 'china', 'mexico', 'brazil', 'australia', 'saudi arabia'
laungage = 'english', 'spanish', 'chinese', 'arabic', 'swahili'
hair_style = 'bold cut', 'bald', 'side part', 'bangs', 'pony tail', 'buzz cut', 'fade', 'bob'
hair_color = 'blond', 'brown', 'black', 'white', 'red', 'orange'
height = "5\'", "5\'1\"", "5\'2\"", "5\'3\"", "5\'4\"", "5\'5\"", "5\'6\"", "5\'7\"", "5\'8\"", "5\'9\"", "5\'10\"", "5\'11\"", "6\'", "6\'1\"", "6\'2\"", "6\'3\"", "6\'4\"", "6\'5\""
def gameStart():
    global name
    name = input("Enter your name to play game\n")
    time.sleep(0.75)
    print("Hello, " +name+ ", this is a game designed to make you cry of confusion")
    time.sleep(2.5)
    print("Sunday, February 11th, 1996, 0400")
    time.sleep(2)
    print("17°51'50\"N 77°17'53\"W\", off the coast of Jamaica") # (fixed)reminder to change the '' to "" before realease
    time.sleep(2)
    print("The weather is a cool, windy wet that kind of reminds your of your home back in Shreveport")
    time.sleep(2)
    print("You're on your boat, the \"Enforcer\", as you named it")
    time.sleep(2)
    print("You swear that 1 day you'll get a new one, since it's your rough 14 year old one")
    time.sleep(2)
    print("\"Should I though?\"")
    time.sleep(2)
    print("\"Do i go to land, or stay here\", you ask yourself")
    time.sleep(1.5)
    print("Do you go to land(1), or not(2)?") # change the (1) and (2) before release
    time.sleep(1)
    goOrNotLandWater()
    
def goOrNotLandWater():
    enter = input("")
    
    if enter == "1":
        wentToLand()
    
    elif enter == "2":
        wentToWater()
    
    elif enter == "back":
        time.sleep(0.5)
        gameStart()
    
    elif enter == "no":
        quit()
        
    else:
        time.sleep(0.5)
        print("Wait, what did you say?")
        time.sleep(0.5)
        goOrNotLandWater()

def wentToLand(): # finish
    time.sleep(1)
    print("\"Here I am, the great island of Jamaica, home of the king, Charles III\"")
    time.sleep(2)
    print("He has been terrorizing the indigenous peoples of the country lately")
    time.sleep(2)
    print("\"And it's your reason to overthrow the monarchy and establish a government.\"")
    time.sleep(2.5)
    print("But first, we must make your character")
    time.sleep(2)
    makeCharacter()

def wentToWater(): # finish
    return

def makeCharacter():
    print(gender)
    global gender1
    gender1 = input("What will your gender be?\n")
    
    if gender1 == "male":
        print("Well then, you are a male")
        time.sleep(2)
        makeChar2()
        
    elif gender1 == "female":
        print("Well then, you are a female")
        time.sleep(2)
        makeChar2()
        
    elif gender1 == "no":
        quit()
    
    elif gender1 == "back":
        time.sleep(1)
        wentToLand()
        
    else:
        print("I don't think I heard you correctly, say that again")
        time.sleep(2)
        makeCharacter()

def makeChar2():
    print(race)
    global race1
    race1 = input("Now choose what race you wish to be\n")
    
    if race1 == "white":
        print("Now you are white")
        time.sleep(1.5)
        makeChar3()
        
    elif race1 == "black":
        print("Now you are black")
        time.sleep(1.5)
        makeChar3()
        
    elif race1 == "asain":
        print("Now you are asain")
        time.sleep(1.5)
        makeChar3()
        
    elif race1 == "hispanic":
        print("Now you are hispanic")
        time.sleep(1.5)
        makeChar3()
        
    elif race1 == "middle eastern":
        print("Now you are middle eastern")
        time.sleep(1.5)
        makeChar3()
        
    elif race1 == "no":
        quit()
        
    elif race1 == "back":
        makeCharacter()
        
    else:
        time.sleep(1)
        print("That's not a race")
        time.sleep(2)
        makeChar2()
        
def makeChar3():
    print(country_of_origin)
    global country
    country = input("What country do you want to be from?\n")
    
    if country == "america":
        print("So you are from america")
        time.sleep(2)
        makeChar4()
        
    elif country == "china":
        print("So you are from china")
        time.sleep(2)
        makeChar4()
        
    elif country == "mexico":
        print("So you are from mexico")
        time.sleep(2)
        makeChar4()
        
    elif country == "brazil":
        print("So you are from brazil")
        time.sleep(2)
        makeChar4()
        
    elif country == "australia":
        print("So you are from australia")
        time.sleep(2)
        makeChar4()
        
    elif country == "saudi arabia":
        print("So you are from saudi arabia")
        time.sleep(2)
        makeChar4()
        
    elif country == "no":
        quit()
        
    elif country == "back":
        time.sleep(1)
        makeChar2()
    
    else:
        print("I'm sorry, but I don't understand")
        time.sleep(2)
        makeChar3()
        
def makeChar4():
    print(name)
    print(gender1)
    print(race1)
    print(country)

gameStart()