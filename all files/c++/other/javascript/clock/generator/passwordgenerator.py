# Imports the time module for time stops
import time
# Imports the random module for randomizing things
import random

# Defines a list for characters to be picked from
lists = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l' 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '$', '%', '^', '&', '*', ';', ':', ',', '.', '>', '<', '/', '?', '|', '-', '_', '=', '+', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z']

# Creates a loop for the main part to be in to restart with everytime
while True:
    # Asks user if they want to generate a password
    ai = input("Generate password?\n")
    
    if ai == "yes":
        # Defines a new line for user input
        def aid():
            # Asks user how many characters they want in their password
            # Allows up to 15 characters max
            ais = input("How many characters? [1 - 15]\n")
            
            if ais == "1":
                print(random.choice(lists))
                
            elif ais == "2":
                print(random.choice(lists), random.choice(lists))
                
            elif ais == "3":
                print(random.choice(lists), random.choice(lists), random.choice(lists))
                
            elif ais == "4":
                print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
            elif ais == "5":
                print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
            elif ais == "6":
                print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
            elif ais == "7":
                print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
            elif ais == "8":
                print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
            elif ais == "9":
                print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
            elif ais == "10":
                print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
            elif ais == "11":
                print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
            elif ais == "12":
                print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
            elif ais == "13":
                print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
            elif ais == "14":
                print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
                
            elif ais == "15":
                print(random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists), random.choice(lists))
            
            # Allows user to go back to the yes or no input
            elif ais == "back":
                return input
                
            elif ais == "no":
                quit()
                
            else:
                aid()
        
        # Starts with the aid() part for password character amount picking        
        aid()
        
    # If user chooses no the loop breaks
    elif ai == "no":
        break
    
    # If the user enters anything other than allowed it restarts the loop
    else:
        time.sleep(0.1)